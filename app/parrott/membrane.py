'''
Membrane
======================
By Francis Tseng (@frnsys)

An interface for content APIs.
'''

import sys
import os
import json
import webbrowser
import tweepy

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def twitter():
	'''
	Authenticates a Twitter account
	and returns a Twitter API object.
	'''

	# Load consumer key & secret from config
	config = json.loads( open(os.path.join(__location__, 'config.json')).read() )
	auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])

	# Authenticate if access key & secret are not set
	if all(key not in config for key in ['access_key', 'access_secret']):
		webbrowser.open(auth.get_authorization_url())

		pin = raw_input('Verification pin number from twitter.com: ').strip()
		token = auth.get_access_token(verifier=pin)

		config['access_key'] = token.key
		config['access_secret'] = token.secret

		with open('config.json', 'w') as outfile:
			outfile.write( yaml.dump(config, default_flow_style=False) )
	else:
		auth.set_access_token(config['access_key'], config['access_secret'])

	# Return API object
	return tweepy.API(auth)
