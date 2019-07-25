from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json, random

from .models import Entity

def rpgHome(request):
    return HttpResponse("RPG Home")

def getRpg(thisSession):
    worlds = {
        'colors' : ['meteor','sunset', 'grade-grey', 'cool-blue', 'ocean', 'clear-sky', 'azure-lane', 'witching-hour'],
        'size' : 'size-400',
    }
    locations = {
        'colors' : ['old-bubblegum'],
        'size' : 'size-200',
    }
    toReturn = {}
    toReturn['entities'] = Entity.objects.filter(is_active=True)
    toReturn['lvl'] = thisSession['lvl']
    toReturn['worldBg'] = random.choice(locations['colors'])
    toReturn['worldSize'] = locations['size']
    return toReturn

def gainExperience(request):
    entityId = request.POST['entityId']
    e = Entity.objects.get(pk=request.POST['entityId'])
    e.experience += int(request.POST['experienceAmount'])
    e.save(update_fields=['experience'])
    return HttpResponse( serializers.serialize('json', [e,]) )
