from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/avidalab/projects/open_projects')
# Create your models here.
class Project( models.Model):

    #we need the name
    name = models.CharField(max_length=255)

    #we would like the extension
    extension = models.CharField(max_length=10)

    #we would like the source
    source = models.FileField(upload_to='projects/%Y/%m/%d')

