'''
Collector
======================
By Francis Tseng (@frnsys)

Collects tweets.
'''

import sys
import membrane

def main():
	twitter = membrane.twitter()

	# Negative
	datafile = open('data/neg.txt', 'wb')

	# Positive
	#datafile = open('data/pos.txt', 'wb')

	# Negative
	users = ["GrahamBlog", "TheScottyNavy", "zzBore", "IngrahamAngle", "limbaugh", "lindsaylohan", "LOHANTHONY", "realcollipark"]

	# Positive
	#users = ["frnsys", "HOLOmagazine", "butdoesitfloat", "synapticstimuli", "killscreen", "atleykins"]

	for user in users:
		for tweet in twitter.user_timeline(screen_name=user, count=200):
			print>>datafile, tweet.text.encode('utf-8')

	return 0

if __name__ == '__main__':
	sys.exit(main())
