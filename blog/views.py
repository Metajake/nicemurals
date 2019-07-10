from django.shortcuts import render
from django.http import HttpResponse

from .models import Entry, Tag

def home(request):
    entries = Entry.objects.all()
    tags = Tag.objects.all()
    context = {
        'entries' : entries,
        'tags' : tags,
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
    context = {
        'entry' : entry,
    }
    return render(request, 'blog/entry.html', context)

def tweetEntry(request):
    print("TWEETING ")
    print(request.POST['content'])
    return HttpResponse('Success!')
