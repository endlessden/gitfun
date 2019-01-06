import unittest
import cap

class TestCap(unittest.TestCase):
	def setup(self):
		pass
	def tear_down(self):
		pass
	def test_one_word(self):
		text = 'duck'
		result = cap.just_do_it(text)
		self.assertEqual(result, 'Duck')


if __name__ == '__main__':
	unittest.main()


