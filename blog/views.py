from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
import random

from blog.functions import tweetEntryLink, getEmptyRowCount, blogBaseProperties
from .models import Entry, Tag, Config
from rpg.views import *

def home(request):
    if 'lvl' not in request.session:
        request.session['lvl'] = 0
    entries = Entry.objects.filter(
        Q(published=True),
        ~Q(tags__tagslug__exact='journal'),
        ~Q(tags__tagslug__exact='devlog'),
    )
    tags = Tag.objects.all()
    rpg = getRpg(request.session)
    config = Config.objects.get(pk=1)
    context = {
        'entries' : entries,
        'tags' : tags,
        'game' : rpg,
        'existance' : 'can-exist' if config.rpg_active else '',
        'worldBg': random.choice(rpg['worldColors'])
    }
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
    context = {**context, **blogBaseProperties}
    return render(request, 'blog/entry.html', context)

def about(request):
    context = {}
    return render(request, 'blog/about.html', context)

def tweetEntry(request):
    tweetEntryLink(None, request.POST)
    e = Entry.objects.get(title=request.POST['title'])
    return HttpResponse(e.tweet_version)
