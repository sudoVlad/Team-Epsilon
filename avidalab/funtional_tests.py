from selenium import webdriver
import unittest
from django.test import TestCase

class HomePageTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    """
    def test_can_start_a_home_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('Home-Page', self.browser.title)
        # self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away
    """

    def test_can_redirect_to_home(self):
        #When we go to localhost:8000 we want to be redirected to lcoalhost:8000/home/

        response = self.client.get('http://localhost:8000')
        self.assertRedirects(response, 'http://localhost:8000/home/', status_code=400, target_status_code=200, host=None, msg_prefix='', \
                        fetch_redirect_response=True)

if __name__ == '__main__':
    unittest.main(warnings='ignore')