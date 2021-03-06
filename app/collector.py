#!/usr/bin/env python

'''
Collector
======================
By Francis Tseng (@frnsys)

Collects tweets.
Run as a cron job.
'''

import sys
from parrott import membrane, memory

def tweets():
    '''
    Collects latest 20 timeline
    tweets for authenticated user.

    Returns:
        List of Tweet texts
    '''
    # Get the Twitter API.
    twitter = membrane.twitter.api()

    # Collect tweets from the authenticated user's timeline.
    tweets = []
    for tweet in twitter.home_timeline():
        tweets.append({
            'tweet': tweet.text,
            'user': tweet.user.screen_name,
            'links': [link['expanded_url'] for link in tweet.entities['urls']],
            'audited': False
            })

    return tweets

def user_tweets( user ):
    '''
    Collect latest 200 tweets from specified user(name).
    '''
    twitter = membrane.twitter.api()
    tweets = [tweet.text.encode('utf-8') for tweet in twitter.user_timeline(screen_name=user, count=200)]
    return tweets

def collect():
    # Store Tweet text into Solr ("memory")
    mem = memory.Memory()
    for tweet in tweets():
        mem.memorize(tweet)
