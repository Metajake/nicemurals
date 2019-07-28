import random

from .models import Entity

def getRpg(thisSession):
    worlds = {
        'colors' : ['meteor','sunset', 'grade-grey', 'cool-blue', 'ocean', 'clear-sky', 'azure-lane', 'witching-hour'],
        'size' : 'size-400',
    }
    locations = {
        'colors' : ['old-bubblegum', 'pomegranite', 'hazy-morning'],
        'size' : 'size-200',
    }
    toReturn = {}
    toReturn['entities'] = Entity.objects.filter(is_active=True)
    toReturn['lvl'] = thisSession['lvl']
    toReturn['worldBg'] = random.choice( [ random.choice(locations['colors']), random.choice(worlds['colors']) ] )
    toReturn['worldSize'] = locations['size']
    return toReturn
