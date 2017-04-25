from django.test import TestCase
from . models import Project
import time
from . models import Project
from django.core.urlresolvers import reverse
# Create your tests here.
import os
import django
from django.db import models

from django.core.files.uploadedfile import SimpleUploadedFile
from . forms import ProjectForm
from . import ParsingData


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
FULLPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class ProjectPageTest(TestCase):

    def setUp(self):
        Project.objects.create(name='Test',source='avidalab/projects/static/test/test.targz' )

    def test_that_project_model(self):
        test_project = Project.objects.create(name='Test2',source='avidalab/projects/static/test/test.targz' )
        test_project.save()
        self.assertTrue(isinstance(test_project, Project))



    #this test makes sure the model is working as intended
    def test_Model(self):
        #test creation of a project
        test_project = Project(name='New',source='avidalab/projects/static/test/test.targz' )
        test_project.save()
        #make sure the fields are filled in properly
        self.assertTrue(test_project.name == 'New')
        self.assertTrue(test_project.decompressed == 'COMPRESSED')

        self.assertTrue(test_project.source == 'avidalab/projects/static/test/test.targz')


    #Test Writing to the server
    def test_file_saving(self):


        #query the database for it
        other_project = Project.objects.get(name='Test')

        #access the fields from the other project
        self.assertTrue(other_project.name == 'Test')
        self.assertTrue(other_project.decompressed == 'COMPRESSED')
        self.assertTrue(other_project.source == 'avidalab/projects/static/test/test.targz')

    def test_file_deletetion(self):

        bool = False
        # query the database for it
        other_project = Project.objects.get(name='Test')
        other_project.delete()
        try:
            other_project = Project.objects.get(name='Test')
        except:
            bool = True
        #self.assertFalse(True)
        self.assertTrue(bool)

    def test_project_delete_page(self):
        # make a test project
        test_project = Project(name='Delete', source='avidalab/projects/static/test/test.targz')
        # save it
        test_project.save()

        # query the database for it
        test_project = Project.objects.get(name='Delete')

        response = self.client.get(reverse('delete', args=(test_project.id,)), follow=True)
        self.assertContains(response, 'Are you sure you want to delete?')

    def test_project_delete_redirect(self):
        # make a test project
        test_project = Project(name='Delete', source='avidalab/projects/testdata/test.targz')
        # save it
        test_project.save()

        # query the database for it
        test_project = Project.objects.get(name='Delete')

        response = self.client.post(reverse('delete', args=(test_project.id,)), follow=True)
        self.assertRedirects(response, reverse('projects'), status_code=302)

    def test_project_edit_page(self):
        # query the database for it
        test_project = Project.objects.get(name='Test')

        response = self.client.get(reverse('edit', args=(test_project.id,)), follow=True)
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Source')

    def test_project_edit_redirect(self):

        # query the database for it
        test_project = Project.objects.get(name='Test')

        response = self.client.post(reverse('edit', args=(test_project.id,)), follow=True)
        self.assertEquals(response.status_code, 200)




    def test_parsing_data_function(self):
        columnNames = ParsingData.parseFile('projects/testdata/dominant.dat')
        dominantColNames = ["Update", "Average Merit of the Dominant Genotype", "Average Gestation Time of the Dominant Genotype", "Average Fitness of the Dominant Genotype", "Repro Rate?", "Size of Dominant Genotype", "Copied Size of Dominant Genotype", "Executed Size of Dominant Genotype", "Abundance of Dominant Genotype", "Number of Births", "Number of Dominant Breed True?", "Dominant Gene Depth", "Dominant Breed In", "Max Fitness?", "Genotype ID of Dominant Genotype", "Name of the Dominant Genotype"]
        self.assertEquals(columnNames, dominantColNames)

    def test_list_posting_data(self):

        test_file = open(os.path.abspath('projects/testdata/test.targz'))
        test_data = {
                    'name':'postTest',
                    'projectFile': test_file
                    }
        response = self.client.post(reverse('projects'),  data=test_data)
        self.assertEquals(response.status_code, 200)

    def test_list_posting_data_validation(self):
        test_file = open(os.path.abspath('projects/testdata/dominant.dat'))
        test_data = {
            'name': 'postTest',
            'projectFile': test_file
        }
        response = self.client.post(reverse('projects'), data=test_data)
        self.assertEquals(response.status_code, 200)