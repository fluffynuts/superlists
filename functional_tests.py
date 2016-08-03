from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
      self.browser = webdriver.Chrome()
      self.browser.implicitly_wait(3)
      
    def tearDown(self):
      self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self): 
      # user atttempts to visit the site
      self.browser.get('http://localhost:8000')
      # user should see 'To-Do' in the browser title
      self.assertIn('To-Do', self.browser.title)

      # user should be invited to create a To-Do item immediately

      # user types in "Buy Cheese". User loves cheese.

      # when the user hits enter, the page updates and now the page
      # lists "1: Buy Cheese" as an item in the todo lists

      # there is still a text box inviting addition of another item

      # user enters "Make a cheese sandwich" (I told you user likes cheese)

      # page updates again -- now there are two items in the list

      # user sees explanatory text about a unique url generated to get back to
      # this To-Do list

      # user visits the special url and the existing to-do items are there

      # user has had an eventful day and really wants some dairy products
      self.fail('test not yet implemented')


if __name__ == '__main__':
  unittest.main()