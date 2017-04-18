from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from . views import index
from . pystats import *
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

    # Math tests
    def test_if_we_can_do_mean(self):
        tempList = [1, 2, 3, 4, 5, 6]
        self.assertEqual(mean(tempList), 3.5)

    def test_if_we_can_do_median_given_unsorted_list(self):
        tempList = [1, 11, 3, 2, 4, 9, 10, 8, 7, 6, 5]
        tempList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.assertEqual(median(tempList), 6)
        self.assertEqual(median(tempList2), 7.5)

    def test_if_we_can_do_standard_deviation(self):
        tempList = [1, 2, 3, 4, 5]
        self.assertEqual(standardDeviation(tempList), math.sqrt(2))

    def test_if_we_catch_tom_foolery(self):
        tempList = [None, None, None]
        tempList2 = ["a", "b", "c"]
        tempList3 = [1, None, 3]
        # check the mean raises errors
        self.assertRaises(TypeError, mean, tempList)
        self.assertRaises(TypeError, mean, tempList2)
        self.assertRaises(TypeError, mean, tempList3)
        # check the median raises errors
        self.assertRaises(TypeError, median, tempList)
        self.assertRaises(TypeError, median, tempList2)
        self.assertRaises(TypeError, median, tempList3)
        # check the standard dev raises errors
        self.assertRaises(TypeError, standardDeviation, tempList)
        self.assertRaises(TypeError, standardDeviation, tempList2)
        self.assertRaises(TypeError, standardDeviation, tempList3)


        # def test_kruskal_Wallace(self):
        # x = [1,3,5,7,9]
        # y = [2,4,6,8,10]
        # self.assertEqual(kruskalWallisH(x,y),(0.27272727272727337,0.60150813444058948))

        # def test_mann_Whitney(self):
        # x = [1,3,5,7,9]
        # y = [2,4,6,8,10]
        # self.assertEqual(mannWhitneyU(x, y), (10.0, 0.33805165701157347))