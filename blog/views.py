from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from itertools import chain

from blog.functions import tweetEntryLink, getEmptyRowCount, getBlogBaseProperties
from .models import Entry, Tag, Config
from rpg.functions import *
from portfolio.models import Project

def home(request):
    if 'lvl' not in request.session:
        request.session['lvl'] = 0

    blogEntries = Entry.objects.filter(published=True)
    projects = Project.objects.all()

    entries = list(chain(projects, blogEntries))

    tags = Tag.objects.all()
    rpg = getRpg(request.session)
    config = Config.objects.get(pk=1)
    context = {
        'entries' : entries,
        'tags' : tags,
        'game' : rpg,
        'existance' : 'can-exist' if config.rpg_active else '',
    }
    blogBaseProperties = getBlogBaseProperties()
    context = {**context, **blogBaseProperties}
    return render(request, 'blog/home.html', context)

def taglist(request, blog_tagslug):
    if 'lvl' in request.session:
        request.session['lvl'] += 1
    entries = Entry.objects.all().filter(tags__tagslug=blog_tagslug)
    tags = Tag.objects.all()
    context = {
        'tag' : Tag.objects.get(tagslug=blog_tagslug),
        'entries' : entries,
        'tags' : tags,
        'existance' : False,
    }
    blogBaseProperties = getBlogBaseProperties()
    context = {**context, **blogBaseProperties}
    return render(request, 'blog/tag_page.html', context)

def entry(request, entry_slug):
    if 'lvl' in request.session:
        request.session['lvl'] += 1
    entry = Entry.objects.get(slug=entry_slug)
    tags = Tag.objects.all()
    context = {
        'entry' : entry,
        'tags' : tags,
        'existance' : False,
    }
    blogBaseProperties = getBlogBaseProperties()
    context = {**context, **blogBaseProperties}
    return render(request, 'blog/entry.html', context)

def about(request):
    context = {}
    blogBaseProperties = getBlogBaseProperties()
    context = {**context, **blogBaseProperties}
    return render(request, 'blog/about.html', context)

def tweetEntry(request):
    tweetEntryLink(None, request.POST)
    e = Entry.objects.get(title=request.POST['title'])
    return HttpResponse(e.tweet_version)
