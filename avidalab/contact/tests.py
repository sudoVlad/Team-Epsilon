from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django import forms
from contact.views import contact

# Create your tests here.
class ContactPageTest(TestCase):
    def test_root_url_resolves_to_contact_page_view(self):
        found = resolve('/contact/')
        self.assertEqual(found.func, contact)

    def test_contact_page_returns_correct_html(self):
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_page_returns_basic_form(self):
        response = self.client.get('/contact/')
        html = response.content.decode('utf8')
        self.assertIn('<form id="contact" action="" method="post">', html)
        self.assertIn('<input placeholder="Your name" type="text" tabindex="1" required autofocus>', html)
        self.assertIn('<input placeholder="Your Email Address" type="email" tabindex="2" required>', html)
        self.assertIn('<input placeholder="Your Phone Number" type="tel" tabindex="3" required>', html)
        self.assertIn('<textarea placeholder="Type your Message Here...." tabindex="5" required></textarea>', html)
        self.assertIn('<button name="submit" type="submit" id="contact-submit" data-submit="...Sending">Submit</button>', html)
