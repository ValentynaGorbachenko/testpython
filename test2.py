import unittest
from selenium import webdriver

class MyTestCase(unittest.TestCase):
	def setUp(self):
		browser = webdriver.Chrome('/Users/Valentynka/Downloads/chromedriver')
		browser.get('http://hrm.seleniumminutes.com')
		self.driver = browser
		print (browser)
		print (self)

	def teatDown(self):
		self.driver.quit()

	def test_something(self):
		browser = self.driver
		browser.find_element_by_id('txtUsername').send_keys('admin')
		browser.find_element_by_id('txtPassword').send_keys('Password')
		browser.find_element_by_id('btnLogin').click()

		greeting_text = browser.find_element_by_id('welcome').text

		self.assertEqual(greeting_text, 'Welcome Admin')

if __name__ == '__main__':
	unittest.main()