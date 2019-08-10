from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Q
from itertools import chain

from blog.functions import tweetEntryLink, getEmptyRowCount, getBlogBaseProperties
from .models import Entry, Tag, Config
from rpg.functions import *
from portfolio.models import Project, Category

def home(request):
    if 'lvl' not in request.session:
        request.session['lvl'] = 0

    projects = Project.objects.filter(is_published=True)
    blogTags = Tag.objects.annotate(num_entries=Count('entry', filter=Q(entry__is_published=True))).filter(num_entries__gte=1)
    projectCategories = Category.objects.annotate(num_entries=Count('project', filter=Q(project__is_published=True))).filter(num_entries__gte=1)
    rpg = getRpg(request.session)
    config = Config.objects.get(pk=1)
    context = {
        'entries' : projects,
        'blog_tags' : blogTags,
        'project_categories' : projectCategories,
        'game' : rpg,
        'existance' : 'can-exist' if config.rpg_active else '',
    }
    blogBaseProperties = getBlogBaseProperties()
    context = {**context, **blogBaseProperties}
    return render(request, 'blog/home.html', context)

def taglist(request, blog_tagslug):
    if 'lvl' in request.session:
        request.session['lvl'] += 1
    entries = Entry.objects.filter(category__tagslug=blog_tagslug)
    blogTags = Tag.objects.annotate(num_entries=Count('entry', filter=Q(entry__is_published=True))).filter(num_entries__gte=1)
    projectCategories = Category.objects.annotate(num_entries=Count('project', filter=Q(project__is_published=True))).filter(num_entries__gte=1)
    context = {
        'headline' : Tag.objects.get(tagslug=blog_tagslug),
        'entries' : entries,
        'blog_tags' : blogTags,
        'project_categories' : projectCategories,
        'existance' : False,
    }
    blogBaseProperties = getBlogBaseProperties()
    context = {**context, **blogBaseProperties}
    return render(request, 'blog/entries_page.html', context)

def categorylist(request, category_slug):
    if 'lvl' in request.session:
        request.session['lvl'] += 1
    projects = Project.objects.filter(category__category_slug=category_slug, is_published=True)
    blogTags = Tag.objects.annotate(num_entries=Count('entry', filter=Q(entry__is_published=True))).filter(num_entries__gte=1)
    projectCategories = Category.objects.annotate(num_entries=Count('project', filter=Q(project__is_published=True))).filter(num_entries__gte=1)
    context = {
        'headline' : Category.objects.get(category_slug=category_slug),
        'entries' : projects,
        'blog_tags' : blogTags,
        'project_categories' : projectCategories,
        'existance' : False,
    }
    blogBaseProperties = getBlogBaseProperties()
    context = {**context, **blogBaseProperties}
    return render(request, 'blog/entries_page.html', context)

def entry(request, entry_slug):
    if 'lvl' in request.session:
        request.session['lvl'] += 1
    entry = Entry.objects.get(slug=entry_slug)
    blogTags = Tag.objects.annotate(num_entries=Count('entry', filter=Q(entry__is_published=True))).filter(num_entries__gte=1)
    projectCategories = Category.objects.annotate(num_entries=Count('project', filter=Q(project__is_published=True))).filter(num_entries__gte=1)
    context = {
        'entry' : entry,
        'blog_tags' : blogTags,
        'project_categories' : projectCategories,
        'existance' : False,
    }
    blogBaseProperties = getBlogBaseProperties()
    context = {**context, **blogBaseProperties}
    return render(request, 'blog/entry.html', context)

def project(request, project_slug):
    p = Project.objects.get(slug=project_slug)
    context = {
        'project': p,
        'column_sizes': ['half','two-thirds'],
    }
    blogBaseProperties = getBlogBaseProperties()
    context = {**context, **blogBaseProperties}
    return render(request, 'blog/project.html', context)

def about(request):
    context = {}
    blogBaseProperties = getBlogBaseProperties()
    context = {**context, **blogBaseProperties}
    return render(request, 'blog/about.html', context)

def tweetEntry(request):
    tweetEntryLink(None, request.POST)
    e = Entry.objects.get(title=request.POST['title'])
    return HttpResponse(e.tweet_version)
