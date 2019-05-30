import unittest, time
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

	def test_valid_login(self):
		browser = self.driver
		time.sleep(3)
		browser.find_element_by_id('txtUsername').send_keys('admin')
		browser.find_element_by_id('txtPassword').send_keys('Password')
		browser.find_element_by_id('btnLogin').click()
		time.sleep(5)

		greeting_text = browser.find_element_by_id('welcome').text

		self.assertEqual(greeting_text, 'Welcome Admin')


if __name__ == '__main__':
	unittest.main()