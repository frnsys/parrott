#!/usr/bin/env python

'''
Collector
======================
By Francis Tseng (@frnsys)

Collects tweets.
'''

import sys
import membrane
from memory import Memory
from pprint import pprint

def tweets():
	'''
	Collects latest 20 timeline
    tweets for authenticated user.

    Returns:
        List of Tweet texts
	'''
	twitter = membrane.twitter.api()

    # Collect tweets and
    # concatenate tweet text and username
	tweets = [' '.join([tweet.text, tweet.user.screen_name]).encode('utf-8')
                for tweet in twitter.home_timeline()]

	return tweets

	# Negative
	#users = ["GrahamBlog", "TheScottyNavy", "zzBore", "IngrahamAngle", "limbaugh", "lindsaylohan", "LOHANTHONY", "realcollipark"]

	# Positive
	#users = ["frnsys", "HOLOmagazine", "butdoesitfloat", "synapticstimuli", "killscreen", "atleykins"]

def user_tweets( user ):
	'''
	Collect latest 200 tweets from specified user(name).
	'''
	twitter = membrane.twitter.api()
	tweets = [tweet.text.encode('utf-8') for tweet in twitter.user_timeline(screen_name=user, count=200)]
	return tweets

def main():
    #memory = Memory()
    for tweet in tweets():
        pprint(tweet)

if __name__ == '__main__':
    sys.exit(main())
