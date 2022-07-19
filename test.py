from unittest import TestCase, main

from palindromes import is_pal

class IsPalindrome(TestCase):
	def test_1_true(self):
		self.assertTrue(is_pal("race car"))
	def test_2_true(self):
		self.assertTrue(is_pal("test tset!"))
	def test_3_true(self):
		self.assertTrue(is_pal("rotator a rotator"))
	def test_4_false(self):
		self.assertFalse(is_pal("not pal!"))
	def test_5_false(self):
		self.assertFalse(is_pal("somemoss"))
	def test_6_false(self):
		self.assertFalse(is_pal("rotator, oh rotator"))
	def test_7_empty(self):
		self.assertTrue(is_pal(""))

if __name__ == '__main__':
	main()