'''
Collector
======================
By Francis Tseng (@frnsys)

Collects tweets.
'''

import membrane
import sunburnt

def tweets():
	'''
	Collects latest timeline tweets
	for authenticated user.
	'''
	twitter = membrane.twitter.api()
	tweets = [tweet.text.encode('utf-8') for tweet in twitter.home_timeline()]
	return tweets

	# Negative
	#users = ["GrahamBlog", "TheScottyNavy", "zzBore", "IngrahamAngle", "limbaugh", "lindsaylohan", "LOHANTHONY", "realcollipark"]

	# Positive
	#users = ["frnsys", "HOLOmagazine", "butdoesitfloat", "synapticstimuli", "killscreen", "atleykins"]

def user_tweets( user ):
	'''
	Collect latest 200 tweets from specified user.
	'''
	twitter = membrane.twitter.api()
	tweets = [tweet.text.encode('utf-8') for tweet in twitter.user_timeline(screen_name=user, count=200)]
	return tweets
