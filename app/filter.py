 #!/usr/bin/env python

import sys
import naive_bayes

def main():
	import csv
	if len(sys.argv) < 2:
		sys.exit('Please supply a CSV to process.')
	filename = sys.argv[1]
	reader = csv.reader(open(filename))
	fields = reader.next()

	'''
	Only collecting the text of retweets.
	The name of the original tweeter is in the text of the retweet,
	so that should represent the original tweeter feature in the classifier.
	'''
	retweet_col = fields.index('retweeted_status_id')
	text_col = fields.index('text')
	retweets = [row[text_col] for row in reader if row[retweet_col]]

	pos_examples = retweets[1::2]
	pos_tests = retweets[::2]

	classifier = NaiveBayes( pos_examples )

	'''
	Might be better to store retweets as CSV, and constantly append to this CSV?
	'''
	#writer = csv.writer(file('retweets.csv', 'wb'), dialect='excel')
	#writer.writerow(retweets)

	return 0

if __name__ == '__main__':
	sys.exit(main())