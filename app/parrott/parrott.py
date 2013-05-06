 #!/usr/bin/env python

import sys
import naive_bayes
import membrane

class Parrott:
	def __init__(self):
		self.brain = naive_bayes.NaiveBayes()
		self.twitter = membrane.twitter()

	def train(self, pos_examples, neg_examples):
		self.brain.train(pos, neg)
		print "foo"

	def test(self, pos_set, neg_set, threshold=0.8):
		return self.brain.test(threshold, pos_set, neg_set)