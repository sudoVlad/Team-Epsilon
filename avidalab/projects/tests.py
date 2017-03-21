from django.test import TestCase
from . models import Project
import time
from . models import Project
from django.core.urlresolvers import reverse
# Create your tests here.
import os
import django


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
FULLPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class ProjectPageTest(TestCase):

    #this test makes sure the model is working as intended
    def test_Model(self):
        #test creation of a project
        test_project = Project(name='Test',extension='txt',source='avidalab/projects/static/test/test.txt' )

        #make sure the fields are filled in properly
        self.assertTrue(test_project.name == 'Test')
        self.assertTrue(test_project.extension == 'txt')
        self.assertTrue(test_project.source == 'avidalab/projects/static/test/test.txt')

    #Test Writing to the server
    def test_file_saving(self):

        #make a test project
        test_project = Project(name='Test', extension='txt', source='avidalab/projects/static/test/test.txt')
        # save it
        test_project.save()

        #query the database for it
        other_project = Project.objects.get(name='Test')

        #access the fields from the other project
        self.assertTrue(other_project.name == 'Test')
        self.assertTrue(other_project.extension == 'txt')
        self.assertTrue(other_project.source == 'avidalab/projects/static/test/test.txt')


    def test_file_in_projec_uploading(self):
        #Creating a file is a special case
        #You must post to the page
        response = self.client.post(
            #reverse gets the right view
            reverse('projects'),

            #This is the JSON??? for the information needed by the upload funciton on the page
            {
                'source': os.path.join(FULLPATH, 'avidalab/projects/static/test/test.txt'),
                'name': 'test',
                'extension':'test'
            },
        )

        #if we get a 200 code we passed the test!
        self.assertEqual(response.status_code, 200, 'Error on create.')


