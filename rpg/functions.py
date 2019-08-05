import random

from .models import Entity

def getRpg(thisSession):
    worlds = {
        'colors' : ['meteor','sunset', 'grade-grey', 'cool-blue', 'ocean', 'clear-sky', 'azure-lane', 'witching-hour'],
        'size' : 'is-size-world',
    }
    locations = {
        'colors' : ['old-bubblegum', 'pomegranite', 'hazy-morning'],
        'size' : 'is-size-location',
    }
    toReturn = {}
    toReturn['entities'] = Entity.objects.filter(is_active=True)
    toReturn['lvl'] = thisSession['lvl']
    environment = random.choice([worlds,locations])
    toReturn['worldBg'] = random.choice( environment['colors'] )
    toReturn['worldSize'] = environment['size']
    return toReturn
