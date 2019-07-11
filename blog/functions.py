from django.db.models.signals import post_save
from django.dispatch import receiver

import tweepy, requests

from blog.models import Entry

@receiver(post_save, sender=Entry)
def tweetEntryLink(sender, instance, **kwargs):
    print("Tweeting Entry Link")
    auth = tweepy.OAuthHandler('wqZDVmeQ0LRjIPblT5N8ZxAQ6', 'SPrk2ifNUZ5SGK6EV04MW41hmKp5yxjDw58In3oAJ4zHEZydoV')
    auth.set_access_token('995766360-5x2RE1NhbEfmzM2hbAuV4vyet4fAqQ1m0FVpQCgY', '8xLHNA40eDYK7vP6SZXqleAPCwNUNcQLN8Jdpxcdrul8L')
    api = tweepy.API(auth)
    # print(instance)
    myStatusText = instance['title'] + ' http://firststudio.co/entry/'+instance['slug']
    api.update_status(status=myStatusText)
