from django.test import TestCase
from . models import Project


# Create your tests here.

class ProjectPageTest(TestCase):

    #this test makes sure the model is working as intended
    def test_Model(self):
        test_project = Project(name='Test',extension='txt',source='avidalab/projects/static/test/test.txt' )
        self.assertTrue(test_project.name == 'Test')
        self.assertTrue(test_project.extension == 'txt')
        self.assertTrue(test_project.source == 'avidalab/projects/static/test/test.txt')

    def test_file_saving(self):
        test_project = Project(name='Test', extension='txt', source='avidalab/projects/static/test/test.txt')
        test_project.save()
        other_project = Project.objects.get(name='Test')
        self.assertTrue(other_project.name == 'Test')
        self.assertTrue(other_project.extension == 'txt')
        self.assertTrue(other_project.source == 'avidalab/projects/static/test/test.txt')

    def test_where_is_that_file(self):
        self.assertTrue(True)