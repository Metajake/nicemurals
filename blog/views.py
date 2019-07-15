from django.shortcuts import render
from django.http import HttpResponse

from blog.functions import tweetEntryLink, getEmptyRowCount
from .models import Entry, Tag, Config
from rpg.views import *

def home(request):
    entries = Entry.objects.filter(published=True)
    tags = Tag.objects.all()
    rpgUpdate = getRpgUpdate()
    config = Config.objects.get(pk=1)
    context = {
        'entries' : entries,
        'tags' : tags,
        'config' : config,
        'game' : rpgUpdate,
    }
    return render(request, 'blog/home.html', context)

def taglist(request, blog_tagslug):
    entries = Entry.objects.all().filter(tags__tagslug=blog_tagslug)
    tags = Tag.objects.all()
    context = {
        'tag' : blog_tagslug,
        'entries' : entries,
        'tags' : tags,
    }
    return render(request, 'blog/taglist.html', context)

def entry(request, entry_slug):
    entry = Entry.objects.get(slug=entry_slug)
    tags = Tag.objects.all()
    context = {
        'entry' : entry,
        'tags' : tags,
    }
    return render(request, 'blog/entry.html', context)

def tweetEntry(request):
    tweetEntryLink(None, request.POST)
    e = Entry.objects.get(title=request.POST['title'])
    return HttpResponse(e.tweet_version)
