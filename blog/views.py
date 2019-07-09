from django.shortcuts import render

from .models import Entry

def home(request):
    entries = Entry.objects.all()
    context = {
        'entries' : entries,
    }
    return render(request, 'blog/home.html', context)
