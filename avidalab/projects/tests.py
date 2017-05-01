from django.test import TestCase
from . models import Project
import time
from . models import Project
from django.core.urlresolvers import reverse
# Create your tests here.
import os
import django
from django.core.files.uploadedfile import SimpleUploadedFile
from . forms import ProjectForm

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
FULLPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class ProjectPageTest(TestCase):
    def generate_file(self):
        try:
            myfile = open('test.csv', 'wb')
        finally:
            myfile.close()

        return myfile

    #this test makes sure the model is working as intended
    def test_Model(self):
        #test creation of a project
        test_project = Project(name='Test',extension='targz',source='avidalab/projects/static/test/test.txt' )

        #make sure the fields are filled in properly
        self.assertTrue(test_project.name == 'Test')
        self.assertTrue(test_project.extension == 'targz')
        self.assertTrue(test_project.source == 'avidalab/projects/static/test/test.txt')

    #Test Writing to the server
    def test_file_saving(self):

        #make a test project
        test_project = Project(name='Test', extension='targz', source='avidalab/projects/static/test/test.txt')
        # save it
        test_project.save()

        #query the database for it
        other_project = Project.objects.get(name='Test')

        #access the fields from the other project
        self.assertTrue(other_project.name == 'Test')
        self.assertTrue(other_project.extension == 'targz')
        self.assertTrue(other_project.source == 'avidalab/projects/static/test/test.txt')


    def test_file_in_projec_uploading(self):
        #Creating a file is a special case
        #You must post to the page
        testfile = self.generate_file()
        file_path = testfile.name
        f = open(file_path, 'rb')
        # Creating a file is a special case
        # You must post to the page

        data = {'source': f, 'name': 'test', 'extension': 'targz', 'decompressed': 'COMPRESSED', }
        response = self.client.post(
            # reverse gets the right view
            reverse('projects'),
            data=data,
        )

        #if we get a 200 code we passed the test!
        self.assertNotContains(response, 'No documents')

    def test_edit_page_loading(self):
        testfile = self.generate_file()
        file_path = testfile.name
        print(os.path.abspath(file_path))
        f = open(file_path, 'rb')

        data = {'source':f, 'name':'test', 'extension':'targz', 'decompressed':'COMPRESSED',}
        # Creating a file is a special case
        # You must post to the page
        response = self.client.post(
            # reverse gets the right view
            '/projects/',
            data=data,
            follow=True
        )
        response = self.client.get('/projects/')
        self.assertNotContains( response, 'No documents')

        project =  Project.objects.all()[0]
        response = self.client.get('edit/' + project.pk, follow=True)

        self.assertEquals(response.status_code, 200)
        os.remove(testfile.name)
        file_path = project.source.path
        os.remove(file_path)

    def test_valid_project_form(self):
        uploadFile = self.generate_file()
        f = open(uploadFile.name, 'rb')
        title = {'name':'test'}
        ext = {'extension': 'none'}
        suf_test = {'projectFile':uploadFile.name}
        comp = {'decompressed': 'COMPRESSED'}
        test_form = ProjectForm(title, suf_test, ext)
        print(test_form.is_valid())
        self.assertTrue(test_form.is_valid())


    def test_parsing_data_function(self):
        columnNames = parseFile('dominant.dat')
        dominantColNames = ["Update", "Average Merit of the Dominant Genotype", "Average Gestation Time of the Dominant Genotype", "Average Fitness of the Dominant Genotype", "Repro Rate?", "Size of Dominant Genotype", "Copied Size of Dominant Genotype", "Executed Size of Dominant Genotype", "Abundance of Dominant Genotype", "Number of Births", "Number of Dominant Breed True?", "Dominant Gene Depth", "Dominant Breed In", "Max Fitness?", "Genotype ID of Dominant Genotype", "Name of the Dominant Genotype"]
        self.assertEquals(columnNames, dominantColNames)

    def test_parsing_data_function_for_dictionary(self):
        dictionary = mapData('dominant.dat')
        self.assertTrue(dictionary)
