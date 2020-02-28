from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        # self.browser.implicitly_wait(5)
    
    def tearDown(self):
        self.browser.quit()
    
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        #user checks to-do app homepage
        self.browser.get('http://localhost:8000')

        #user notices page title and header
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        #the user types 'buy milk' into a text box
        inputbox.send_keys('Buy milk')

        #when the user hits enter, the page updates
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1:Buy milk')

        #the user is invited to add another item
        inputbox =self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Do homework')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #page updates and show both items on the lists
        self.check_for_row_in_list_table('1:Buy milk')
        self.check_for_row_in_list_table('2:Do homework')

        self.fail('Finish the test.')

if __name__ == '__main__':
    unittest.main(warnings='ignore')