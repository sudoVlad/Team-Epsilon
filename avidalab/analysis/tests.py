from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from . views import index
# Create your tests here.
class analysisTestCase(TestCase):
    def test_analysis_url_resolves_to_analysis_page(self):
        found = resolve('/analysis/')
        self.assertEqual(found.func, index)
    def test_analysis_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertIn('<button>Run Statistics</button>',html)
        self.assertIn('<button>Generate Graphs</button>',html)
        self.assertIn('<button>Export</button>',html)

