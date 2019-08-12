from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.conf import settings
import random

import tweepy, requests, inspect

from blog.models import Entry, Config

blogOptions = {
    'homeAnchorIcons' : [
        ('fas', 'fa-car-side'),
        ('fas', 'fa-blind'),
        ('fas', 'fa-car-crash'),
        ('fas', 'fa-baby-carriage'),
        ('fas', 'fa-people-carry'),
        ('fas', 'fa-truck-pickup'),
        ('fas', 'fa-dolly'),
        ('fab', 'fa-accessible-icon'),
    ],
    'favIcons' : ['cone', 'cube', 'elipse', 'diamond', 'trapezoid', 'trapezoid2', 'star', 'star2', 'star3',],
}

def getBlogBaseProperties():
    config = Config.objects.get(pk=1)
    toReturn = {
        'entry_sort_type' : 'columns' if config.entry_sorting == 'columns' else 'tile',
        'home_icon': random.choice(blogOptions['homeAnchorIcons']),
        'favicon': random.choice(blogOptions['favIcons']),
        'language':random.choice(['ja','en'])
    }
    return toReturn

#THIS GETS FIRED WHETHER YOU SAVE AN ENTRY FROM THE ADMIN OR FROM THIS FILE LINE 28 (HITTING THE TEMPLATE TWEET BUTTON)
@receiver(pre_save, sender=Entry)
def incrementTweetVersion(sender, instance, **kwargs):
    instance.tweet_version = instance.tweet_version + 1

@receiver(post_save, sender=Entry)
def tweetEntryLink(sender, instance, **kwargs):
    auth = tweepy.OAuthHandler('wqZDVmeQ0LRjIPblT5N8ZxAQ6', 'SPrk2ifNUZ5SGK6EV04MW41hmKp5yxjDw58In3oAJ4zHEZydoV')
    auth.set_access_token('995766360-5x2RE1NhbEfmzM2hbAuV4vyet4fAqQ1m0FVpQCgY', '8xLHNA40eDYK7vP6SZXqleAPCwNUNcQLN8Jdpxcdrul8L')
    api = tweepy.API(auth)

    #Hack: Check if Instance has title property (in other words, check if it's a Real Django Database Class instance (not an ajax object))
    try:
        myStatusText = instance.title + " v" + str(instance.tweet_version) + ' http://firststudio.co/entry/'+instance.slug
    except AttributeError:
        e = Entry.objects.get(title=instance['title'])
        e.save( update_fields=['tweet_version'] )
        myStatusText = instance['title'] + " v" + str(instance['tweet_version']) + ' http://firststudio.co/entry/'+instance['slug']

    try:
        if settings.DEBUG == False:
            if instance.fire_laser:
                api.update_status(status=myStatusText)
    except:
        print("ERROR TWEETING")
        pass

def getEmptyRowCount(totalEntries, rowTotalCount):
    if totalEntries < rowTotalCount:
        emptyCards = rowTotalCount - totalEntries #to fill in template row
    else:
        emptyCards = rowTotalCount - (totalEntries % rowTotalCount) #to fill in template row
    return emptyCards
