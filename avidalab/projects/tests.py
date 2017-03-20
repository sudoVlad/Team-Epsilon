from django.test import TestCase
from . models import Project


# Create your tests here.

class ProjectPageTest(TestCase):

    #this test makes sure the model is working as intended
    def test_Model(self):
        test_project = Project(name='Test',extension='txt',source='avidalab/projects/static/test/test.txt' )
        self.assertTrue(test_project.name == 'Test')
        print(test_project.extension)
        self.assertTrue(test_project.extension == 'txt')
        self.assertTrue(test_project.source == 'avidalab/projects/static/test/test.txt')