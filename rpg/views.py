from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json

from .models import Entity

def rpgHome(request):
    return HttpResponse("RPG Home")

def getRpgUpdate(thisSession):
    toReturn = {}
    toReturn['entities'] = Entity.objects.filter(is_active=True)
    toReturn['lvl'] = thisSession['lvl']
    return toReturn

def gainExperience(request):
    entityId = request.POST['entityId']
    e = Entity.objects.get(pk=request.POST['entityId'])
    e.experience += int(request.POST['experienceAmount'])
    e.save(update_fields=['experience'])
    return HttpResponse( serializers.serialize('json', [e,]) )
