from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from selenium import webdriver
from django.urls import reverse
from django.urls import resolve


class HomePageTest(TestCase):

    def test_those_buttons(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, '<a href="%s">Home</a>' % reverse("index"), html=True)

        response = self.client.get(reverse("index"))
        self.assertContains(response, '<a href="%s">Import</a>' % reverse("import"), html=True)

        response = self.client.get(reverse("index"))
        self.assertContains(response, '<a href="%s">Analysis</a>' % reverse("analysis"), html=True)

        response = self.client.get(reverse("index"))
        self.assertContains(response, '<a href="%s">Contact</a>' % reverse("contact"), html=True)
