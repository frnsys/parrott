'''
Parrott
======================
By Francis Tseng (@frnsys)

A pseudo-intelligent auto-retweeter.
'''

import sys
import naive_bayes
import membrane
from memory import Memory

class Parrott:
	def __init__(self):
		self.brain = naive_bayes.NaiveBayes()
		self.twitter = membrane.twitter.api()
        self.memory = Memory()

	def train(self, pos_examples, neg_examples):
		self.brain.train(pos, neg)

	def test(self, pos_set, neg_set, threshold=0.8):
		return self.brain.test(threshold, pos_set, neg_set)