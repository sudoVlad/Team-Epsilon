from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.
class Project( models.Model):

    #we need the name
    name = models.CharField(max_length=255)

    #we would like the extension
    extension = models.CharField(max_length=10)

    #we would like the source
    #the project source should be today's date and the name of the file
    source = models.FileField(upload_to='projects/%Y/%m/%d/')

    #to be used by the unzip function you can dump the unzip directory here
    #unzip the archive source into a new folder in the 'projects/%Y/%m/%d/' directory
    #that it is located on. then make a new folder in that directory which is the name of
    #the project. Then dump the new zipped runs into here.
    decompressed = models.CharField(max_length=255)



