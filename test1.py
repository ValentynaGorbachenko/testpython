import unittest 
import foo
class MyTestCase(unittest.TestCase):
	def test_something(self):
		# print(type(self))
		self.assertEqual(True, False)
		foo() # understading __name__ == '__main__'

if __name__ == '__main__':
	unittest.main()