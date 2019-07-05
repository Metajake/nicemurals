from django.shortcuts import render

from .models import Work

def home(request):
    works = Work.objects.filter(is_enabled=True)
    context = {
        'works': works,
    }
    return render(request, 'portfolio/home.html', context)
