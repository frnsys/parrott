'''
Twitter
======================
By Francis Tseng (@frnsys)
'''

import webbrowser
import tweepy

import os
import simplejson as json
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def api():
	'''
	Authenticates a Twitter account
	and returns a Twitter API object.
	'''

	# Load consumer key & secret from config
	config = json.loads( open(os.path.join(__location__, 'config.json')).read() )
	twitter = config['twitter']
	auth = tweepy.OAuthHandler(twitter['consumer_key'], twitter['consumer_secret'])

	# Authenticate if access key & secret are not set
	if all(key not in twitter for key in ['access_key', 'access_secret']):
		webbrowser.open(auth.get_authorization_url())

		pin = raw_input('Verification pin number from twitter.com: ').strip()
		token = auth.get_access_token(verifier=pin)

		config['twitter']['access_key'] = token.key
		config['twitter']['access_secret'] = token.secret

		with open('config.json', 'w') as outfile:
			outfile.write( yaml.dump(config, default_flow_style=False) )
	else:
		auth.set_access_token(twitter['access_key'], twitter['access_secret'])

	# Return API object
	return tweepy.API(auth)
