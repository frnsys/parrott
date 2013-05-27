#!/usr/bin/env python

import unittest
from parrott import Parrott

class Test(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_parrott(self):
		p = Parrott()
		self.assertIsInstance(p, Parrott)

if __name__ == '__main__':
	unittest.main()
