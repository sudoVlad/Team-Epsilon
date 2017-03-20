from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django import forms
from contact.views import contact
from .forms import ContactForm

# Create your tests here.
# Tests for the Contact Page
class ContactPageTest(TestCase):
    def test_contact_form(self):
        form_data = {'name': 'some name', 'phone': '111-111-1111',
                        'email': 'example@example.com',
                        'subject': 'some subject', 'message': 'some message'}
        form = ContactForm(data = form_data)
        self.assertTrue(form.is_valid())

    def test_contact_page_returns_correct_html(self):
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_page_returns_correct_contact_form_html(self):
        response = self.client.get('/contact/')
        html = response.content.decode('utf8')
        self.assertIn('<form method="post">', html)
        self.assertIn('<h2>Contact us by filling out the form below</h2>', html)
        self.assertIn('<fieldset>', html)
        self.assertIn('</fieldset>', html)
        self.assertIn('<div class="form-actions">', html)
        self.assertIn('<button type="submit">Send</button>', html)
