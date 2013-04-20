 #!/usr/bin/env python

import sys
import naive_bayes
import membrane

def main():
	'''
	Temporary just loading latest stream as 
	negative examples.
	'''
	twitter = membrane.twitter()
	neg = [example.strip() for example in open("data/neg.txt").readlines()]
	pos = [example.strip() for example in open("data/pos.txt").readlines()]


	'''
	Split data into test and training sets
	'''
	pos_examples = pos[1::2]
	pos_tests = pos[::2]

	neg_examples = neg[1::2]
	neg_tests = neg[::2]
	print "Training on %i positive examples" % len(pos_examples)
	print "Training on %i negative examples" % len(neg_examples)

	classifier = naive_bayes.NaiveBayes( pos_examples, neg_examples )
	classifier.train()
	#print classifier.classify("A thought-provoking digital art project - Energy Flow made it into The Guardian's 30 best Android apps of the week!")

	print classifier.test(0.8, pos_tests, neg_tests)

	return 0

if __name__ == '__main__':
	sys.exit(main())