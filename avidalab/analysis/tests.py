from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from . pystats import *
from . views import mean_array_maker
from django.core.urlresolvers import reverse
import os
from os import listdir

from projects.models import Project
# Create your tests here.
class analysisTestCase(TestCase):


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

    def test_context_data_from_view(self):

        #first we must setup the test project
        test_project = Project(name='TestThis',source='avidalab/projects/static/test/test.targz', decompressed=os.path.abspath('projects/testdata/testProject' ))
        print(test_project.decompressed)
        test_project.save()
        test_project = Project.objects.get(name='TestThis')
        response = self.client.get(reverse('analyze', args=(test_project.id,)), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_mean_array_maker(self):
        #test same length
        arrays = [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5]
        ]
        expected = [1.,2.,3.,4.,5.]
        self.assertListEqual(mean_array_maker(arrays).tolist(), expected )


        #test variable length
        arrays = [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4]
        ]
        expected = [1, 2, 3, 4]
        self.assertListEqual(mean_array_maker(arrays).tolist(), expected)

    def test_analysis_redirect(self):
        response = self.client.get(reverse('analysis'))
        self.assertEqual(response.status_code, 200)

    def test_analysis_detail_redirect(self):
        #make sure the test project is proper
        Project.objects.create(name='Test', source='avidalab/projects/static/test/test.targz',
                               decompressed=os.path.abspath('projects/testdata/testProject'))
        tp = Project.objects.get(name='Test')
        response = self.client.get(reverse('analyze', args=[tp.id]))
        self.assertEqual(response.status_code, 200)
        runs = listdir(tp.decompressed)
        self.assertListEqual(response.context_data['exps'], runs)

    def test_analysis_runs_redirect(self):
        #make sure the test project is proper
        Project.objects.create(name='Test', source='avidalab/projects/static/test/test.targz',
                               decompressed=os.path.abspath('projects/testdata/testProject'))
        tp = Project.objects.get(name='Test')
        data = {'exp': 'exp1',
                'projectID':tp.id
                }
        response = self.client.get(reverse('analyzeRun'), data=data)
        self.assertEqual(response.status_code, 200)

    def test_analysis_field_redirect_no_runs(self):
        #make sure the test project is proper
        Project.objects.create(name='Test', source='avidalab/projects/static/test/test.targz',
                               decompressed=os.path.abspath('projects/testdata/testProject'))
        tp = Project.objects.get(name='Test')
        data = {'exp':'exp1',
                'projectID' : tp.id ,
                }
        response = self.client.get(reverse('analysisField'), data=data)
        self.assertEqual(response.status_code, 302)

    def test_analysis_field_redirect(self):
        #make sure the test project is proper
        Project.objects.create(name='Test', source='avidalab/projects/static/test/test.targz',
                               decompressed=os.path.abspath('projects/testdata/testProject'))
        tp = Project.objects.get(name='Test')
        data = {'exp':'exp1',
                'projectID' : tp.id ,
                'selectedRuns' : ['run_1'],
                'selectedData' : 'dominant.dat'
                }
        response = self.client.get(reverse('analysisField'), data=data)
        self.assertEqual(response.status_code, 200)

    def test_analysis_graphs_redirect(self):
        # make sure the test project is proper
        Project.objects.create(name='Test', source='avidalab/projects/static/test/test.targz',
                               decompressed=os.path.abspath('projects/testdata/testProject'))
        tp = Project.objects.get(name='Test')
        data = {'exp': 'exp1',
                'projectID': tp.id,
                'newRuns': ['run_1'],
                'data': 'dominant.dat',
                'selectedField' : 'Update'
                }
        response = self.client.get(reverse('graphs'), data=data)
        self.assertEqual(response.status_code, 200)


    def test_analysis_stats_redirect(self):
        # make sure the test project is proper
        Project.objects.create(name='Test', source='avidalab/projects/static/test/test.targz',
                               decompressed=os.path.abspath('projects/testdata/testProject'))
        tp = Project.objects.get(name='Test')
        data = {'exp': 'exp1',
                'projectID': tp.id,
                'newRuns': ['run_1'],
                'data': 'dominant.dat',
                'selectedField' : 'Update'
                }
        response = self.client.get(reverse('stats'), data=data)
        self.assertEqual(response.status_code, 200)
