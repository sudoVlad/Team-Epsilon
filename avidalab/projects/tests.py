from django.test import TestCase
from . models import Project
import time
from . models import Project
# Create your tests here.

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

    #This test should beable to go to the download link for the file
    def test_where_is_that_file(self):
        #create a test project
        test_project = Project(name='Test', extension='txt', source='avidalab/projects/static/test/test.txt')


        #print(test_project)
        #save it
        test_project.save()

        #Access the test project
        other_project = Project.objects.get(name='Test')
        print(other_project.source.url)

        #go to the URL for the queryed projects file
        response = self.client.get(other_project.source.url , follow=True)
        #print(other_project.source.url)
        self.assertEquals(response.status_code, 200)
        #self.assertTrue(True)