from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from selenium import webdriver
from home.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_url_working(self):
        self.browser = webdriver.Firefox()
        self.browser.get('https://media.giphy.com/media/M7gtacN7aPNsc/giphy.gif')
        self.assertIn('giphy', self.browser.title)
        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.get('http://www.obeythetestinggoat.com/book/images/twdp_0401.png')
        self.assertIn('twdp', self.browser.title)
        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.get('https://www.youtube.com/embed/ZZ5LpwO-An4?autoplay=1')
        self.assertIn('HEYYEYAAEYAAAEYAEYAA', self.browser.title)
        self.browser.quit()

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Home-Page</title>', html)
        self.assertIn('<BODY><IMG SRC="https://media.giphy.com/media/M7gtacN7aPNsc/giphy.gif"></BODY>', html)
        self.assertIn('<BODY><IMG SRC="http://www.obeythetestinggoat.com/book/images/twdp_0401.png"></BODY>', html)
        self.assertIn('<iframe width="1" height="1" src="https://www.youtube.com/embed/ZZ5LpwO-An4?autoplay=1" frameborder="0" allowfullscreen></iframe>', \
                       html)
        self.assertTrue(html.endswith('</html>'))