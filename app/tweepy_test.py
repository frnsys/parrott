#!/usr/bin/env python

import sys
import yaml
import webbrowser
import tweepy

def main():
	config = yaml.load(open('config.yml'))

	if all(key not in config for key in ['access_key', 'access_secret']):
		auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
		webbrowser.open(auth.get_authorization_url())

		pin = raw_input('Verification pin number from twitter.com: ').strip()
		token = auth.get_access_token(verifier=pin)

		config['access_key'] = token.key
		config['access_secret'] = token.secret

		with open('config.yml', 'w') as outfile:
			outfile.write( yaml.dump(config, default_flow_style=False) )
	else:
		print "already authed"

if __name__ == '__main__':
	sys.exit(main())
