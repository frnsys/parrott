'''
Naive Bayes Classifier
======================
By Francis Tseng (@frnsys)

Ported/adapted from Edwin Chen's Ruby Naive Bayes Classifer
http://goo.gl/uLmBf
'''

import collections
import re

class NaiveBayes:
	def __init__(self):
		self.probs = {}

	def train(self, pos_examples, neg_examples, ngram_size=1):
		'''
		Trains the classifier

        Args:
            pos_examples (list): the positive example documents
            neg_examples (list): the negative example documents
            ngram_size (int): size of the ngrams
		'''

		self.ngram_size = ngram_size
		self.pos_examples = pos_examples
		self.neg_examples = neg_examples

        # Get the counts for each ngram in each document set.
		self.pos_counts = self._get_ngram_counts(self.pos_examples)
		self.neg_counts = self._get_ngram_counts(self.neg_examples)

        # Get the total count of positive and negative ngrams.
		pos_total_count = sum(self.pos_counts.itervalues())
		neg_total_count = sum(self.neg_counts.itervalues())

        # Iterate over all the ngrams, from both sets.
		for ngram in set(self.pos_counts.keys() + self.neg_counts.keys()):
            # Calculate the probability of this ngram being positive,
            # and the probability of this ngram being negative.
			pos_p = float(self.pos_counts[ngram]) / pos_total_count
			neg_p = float(self.pos_counts[ngram]) / neg_total_count
			self.probs[ngram] = [pos_p, neg_p]


	def test(self, threshold, pos_test_examples, neg_test_examples):
		'''
		Tests the classifier

		Args:
			threshold (float): the threshold for a positive classification
			pos_test_examples (list): the positive test documents
			neg_test_examples (list): the negative test documents
		Returns:
			Dictionary of true positives, false positives, true negatives, and false negatives
		'''

        # True positive, false positive, true negative, false negative.
		tp = fp = tn = fn = 0

        # For each document in the positive test examples...
		for doc in pos_test_examples:
            # Classify and compare result to the specified threshold.
			if self.classify(doc) > threshold:
                # The classifier recognizes that this is positive.
				tp += 1
			else:
                # The classifier did not recognize that this is positive.
				fn += 1

        # For each document in the negative test examples...
		for doc in neg_test_examples:
            # Classify and compare result to the specified threshold.
			if self.classify(doc) < threshold:
                # The classifier recognizes that this is negative.
				tn += 1
			else:
                # The classifier did not recognize that this is negative.
				fp += 1

		return {'true positives': tp,
				'false positives': fp,
				'true negatives': tn,
				'false negatives': fn}
	

	def best_pos_predictors(self):
		'''
		Calculates best positive classification predictors

		Returns:
			List of best positive classification predictors
		'''
        # Get total positive ngram count.
		total_pos_count = sum(self.pos_counts.itervalues())

        # Sort by probabilities [pos,neg] by pos/(pos+neg)
		sorted_list = sorted(self.probs.items(), key=lambda (k,v): v[0] / sum(v))

        # Filter the sorted list to include only ngrams
        # that have a positive count > 10.
		filtered_list = filter(lambda (k,v): self.pos_counts[k] > 10, sorted_list)
		return list(reversed(filtered_list))[:500]

	def best_neg_predictors(self):
		'''
		Calculates best negative classification predictors

		Returns:
			List of best negative classification predictors
		'''

        # Get total negative ngram count.
		total_neg_count = sum(self.neg_counts.itervalues())

        # Sort by probabilities [pos,neg] by neg/(pos+neg)
		sorted_list = sorted(self.probs.items(), key=lambda (k,v): v[1] / sum(v))

        # Filter the sorted list to include only ngrams
        # that have a negative count > 10.
		filtered_list = filter(lambda (k,v): self.neg_counts[k] > 10, sorted_list)
		return list(reversed(filtered_list))[:500]

	def classify(self, doc):
		'''
		Classifies a document.

		Args:
			doc (string): the document to classify
		Returns:
			The probability of positive classification
		'''

        # Retrieve the pos/neg probabilities for each ngram
        # in the specified doc.
        # Set probability=[0.5,0.5] if no data is available for that ngram.
		probs = [self.probs.setdefault(ngram, [0.5,0.5])
				for ngram in self._to_ngrams(doc)]

		if not probs: return 0

        # Calculate the product of all positive probabilities,
        # and the product of all negative probabilities.
        # Note: `reduce` performs a specified operation, here x*y,
        # going down a list: http://bit.ly/11HHsmx
		pos_probs = reduce(lambda x,y: x*y, [prob[0] for prob in probs])
		neg_probs = reduce(lambda x,y: x*y, [prob[1] for prob in probs])
		return pos_probs / (pos_probs + neg_probs)
		

	# Private
	def _get_ngram_counts(self, docs):
		'''
		Counts ngram occurences in a set of documents

		Args:
			docs (list): the documents to count
		Returns:
			A hash of the ngrams and their counts
		'''

		# Add-one smoothing.
		counts = collections.defaultdict(lambda: 1)

        # For each document...
		for doc in docs:
            # Count the ngrams.
			for ngram in self._to_ngrams(doc):
				counts[ngram] += 1

		return counts


	def _to_ngrams(self, doc):
		'''
		Normalizes and converts a document into ngrams of size n

		Args:
			doc (string): the document to convert
		Returns:
			A list of the ngrams
		'''

		ngrams = list()
		normalized = self._normalize(doc).split()

		# Iterate over the normalized doc in chunks,
        # where each chunk is of ngram_size.
		# http://goo.gl/2bYCD
		for chunk in map(None, *(iter(normalized),)*self.ngram_size):
            # If ngram size is > 1, join the tokens with a space.
			if self.ngram_size > 1:
				ngrams.append(' '.join(chunk))
			else:
				ngrams.append(chunk)

		return ngrams


	def _normalize(self, doc):
		'''
		Normalizes a document

		Args:
			doc (string): the document to normalize
		Returns:
			The normalized document
		'''

        # Lowercase the doc, and clean it up.
		_doc = re.sub(r'[^a-z0-9\s]', '', doc.lower())

        # If the ngrams are larger than 1,
        # need to append START and END tokens to the doc.
		if self.ngram_size > 1:
			_doc = 'START ' + _doc + ' END'

        # Compress extra whitespace.
		_doc = re.sub(r'\s+', ' ', _doc)

		return _doc


