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
