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



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
FULLPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTSOURCE = 'projects/testdata/test.zip'
class ProjectPageTest(TestCase):

    def setUp(self):
        Project.objects.create(name='Test',source=TESTSOURCE)

    def test_that_project_model(self):
        test_project = Project.objects.create(name='Test2',source=TESTSOURCE )
        test_project.save()
        self.assertTrue(isinstance(test_project, Project))



    #this test makes sure the model is working as intended
    def test_Model(self):
        #test creation of a project
        test_project = Project(name='New',source=TESTSOURCE )
        test_project.save()
        #make sure the fields are filled in properly
        self.assertTrue(test_project.name == 'New')
        self.assertTrue(test_project.decompressed == 'COMPRESSED')

        self.assertTrue(test_project.source == TESTSOURCE)


    #Test Writing to the server
    def test_file_saving(self):


        #query the database for it
        other_project = Project.objects.get(name='Test')

        #access the fields from the other project
        self.assertTrue(other_project.name == 'Test')
        self.assertTrue(other_project.decompressed == 'COMPRESSED')
        self.assertTrue(other_project.source == TESTSOURCE)

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
        test_project = Project(name='Delete', source=TESTSOURCE)
        # save it
        test_project.save()

        # query the database for it
        test_project = Project.objects.get(name='Delete')

        response = self.client.get(reverse('delete', args=(test_project.id,)), follow=True)
        self.assertContains(response, 'Are you sure you want to delete?')

    def test_project_delete_redirect(self):
        # make a test project
        test_project = Project(name='Delete', source=TESTSOURCE)
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


    def test_project_unzip_reirect(self):
        test_project = Project.objects.get(name='Test')

        response = self.client.post(reverse('unzip', args=(test_project.id,)), follow=True)
        self.assertEquals(response.status_code, 200)



    def test_list_posting_data(self):

        test_file = open(os.path.abspath('projects/testdata/test.zip'))
        test_data = {
                    'name':'postTest',
                    'projectFile': test_file
                    }
        response = self.client.post(reverse('projects'),  data=test_data)
        self.assertEquals(response.status_code, 302)

    def test_list_posting_data_validation(self):
        test_file = open(os.path.abspath('projects/testdata/dominant.dat'))
        test_data = {
            'name': 'postTest',
            'projectFile': test_file
        }
        response = self.client.post(reverse('projects'), data=test_data)
        self.assertEquals(response.status_code, 200)

