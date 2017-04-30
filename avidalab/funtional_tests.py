import selenium
import unittest
from django.test import TestCase
from django.urls import reverse
from django.urls import resolve

class HomePageTest(TestCase):
    def test_urls_go_to_the_right_place(self):
        #ensure we can connect with a / root
        response = self.client.get('/', follow=True)

        self.assertEquals(response.status_code, 200)

        # ensure we can connect with a /home/ root
        response = self.client.get('/home/', follow=True)
        #print(response.redirect_chain)
        self.assertEquals(response.status_code, 200)




class ContactPageTestCase(TestCase):


    def test_root_url_resolves_to_contact_page_view(self):
        found = self.client.get('/contact/', follow=True)
        #print(found.redirect_chain)
        self.assertEqual(found.status_code, 200)

        #now lets try that with some post data
        data = {'name':'test',
                'phone' : '3333333333',
                'email' : 'something@gmail.com',
                'subject': 'test subject',
                'message' : 'test',
                }

        found = self.client.post('/contact/', data , follow=True)
        # print(found.redirect_chain)
        self.assertEqual(found.status_code, 200)

class AnalysisPageTestCase(TestCase):


    def test_urls_go_to_the_right_place(self):
        #test if /analysis goes to the analysis page
        response = self.client.get('/analysis/', follow=True)
        #print(response)
        self.assertEquals(response.status_code, 200)

class ProjectsPageTestCase(TestCase):

    def test_urls_go_to_the_right_place(self):
        # test if /projects/ goes to the project page
        response = self.client.get('/projects/', follow=True)
        # print(response)
        self.assertEquals(response.status_code, 200)


        # print(response)
        #self.assertEquals(response.status_code, 404)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
