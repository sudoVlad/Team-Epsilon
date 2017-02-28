from selenium import webdriver
import unittest
from django.test import TestCase
from django.urls import reverse
from django.urls import resolve

class HomePageTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
      self.browser.quit()


    def test_urls_go_to_the_right_place(self):
        #ensure we can connect with a / root
        response = self.client.get('/', follow=True)
        print(response.redirect_chain)
        self.assertEquals(response.status_code, 200)

        # ensure we can connect with a /home/ root
        response = self.client.get('/home/', follow=True)
        print(response.redirect_chain)
        self.assertEquals(response.status_code, 200)

        #Make sure we can connect to the home page
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)





if __name__ == '__main__':
    unittest.main(warnings='ignore')