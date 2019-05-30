import unittest, time
from selenium import webdriver

'''
Using the valid login example test case created in class, create negative test cases for the login functionality.
0) Valid login
1) Invalid username
2) Empty username
3) Invalid password
4) Empty password
5) Leading or trailing white-space in password
'''
class Login(unittest.TestCase):
	def setUp(self):
		browser = webdriver.Chrome('/Users/Valentynka/Downloads/chromedriver')
		browser.get('http://hrm.seleniumminutes.com')
		self.driver = browser

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

	def test_invalid_username(self):
		browser = self.driver
		browser.find_element_by_id('txtUsername').send_keys('admi')
		browser.find_element_by_id('txtPassword').send_keys('Password')
		browser.find_element_by_id('btnLogin').click()

		warning_text = browser.find_element_by_id('spanMessage').text
		self.assertEqual('Invalid credentials', warning_text)
		time.sleep(2)

	def test_empty_username(self):
		browser = self.driver
		browser.find_element_by_id('txtUsername').send_keys('')
		browser.find_element_by_id('txtPassword').send_keys('Password')
		browser.find_element_by_id('btnLogin').click()

		warning_text = browser.find_element_by_id('spanMessage').text
		self.assertEqual('Username cannot be empty', warning_text)
		time.sleep(2)

	def test_invalid_passord(self):
		browser = self.driver
		browser.find_element_by_id('txtUsername').send_keys('admin')
		browser.find_element_by_id('txtPassword').send_keys('password')
		browser.find_element_by_id('btnLogin').click()

		warning_text = browser.find_element_by_id('spanMessage').text
		self.assertEqual('Invalid credentials', warning_text)
		time.sleep(2)

	def test_empty_passord(self):
		browser = self.driver
		browser.find_element_by_id('txtUsername').send_keys('admin')
		browser.find_element_by_id('txtPassword').send_keys('')
		browser.find_element_by_id('btnLogin').click()

		warning_text = browser.find_element_by_id('spanMessage').text
		self.assertEqual('Password cannot be empty', warning_text)
		time.sleep(2)

	def test_white_spaces_leading_passord(self):
		browser = self.driver
		browser.find_element_by_id('txtUsername').send_keys('admin')
		browser.find_element_by_id('txtPassword').send_keys(' password')
		browser.find_element_by_id('btnLogin').click()

		warning_text = browser.find_element_by_id('spanMessage').text
		self.assertEqual('Invalid credentials', warning_text)
		time.sleep(2)

	def test_white_spaces_trailing_passord(self):
		browser = self.driver
		browser.find_element_by_id('txtUsername').send_keys('admin')
		browser.find_element_by_id('txtPassword').send_keys('password ')
		browser.find_element_by_id('btnLogin').click()

		warning_text = browser.find_element_by_id('spanMessage').text
		self.assertEqual('Invalid credentials', warning_text)
		time.sleep(2)

if __name__ == '__main__':
	unittest.main()

