from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setup(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        #user checks to-do app homepage
        self.browser.get('http://localhost:8000')

        #user notices page title and header
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        #user is invited to enter a to-do item

if __name__ == '__main__':
    unittest.main(warnings='ignore')