from django.db import models
from django.core.exceptions import ValidationError

'''
def validate_file_extension(value):
    print('doing this thing here ***************')
    if not value.name.endswith('.targz'):
        raise ValidationError(u'Error message')
'''

# Create your models here.
class Project( models.Model):


    #we need the name
    name = models.CharField(max_length=255)


    #we would like the source
    #the project source should be today's date and the name of the file
    source = models.FileField(upload_to='projects/%Y/%m/%d/')

    #to be used by the unzip function you can dump the unzip directory here
    #unzip the archive source into a new folder in the 'projects/%Y/%m/%d/' directory
    #that it is located on. then make a new folder in that directory which is the name of
    #the project. Then dump the new zipped runs into here.
    decompressed = models.CharField(max_length=900, default='COMPRESSED')

    def delete(self, *args, **kwargs):
        self.source.delete()
        super(Project, self).delete(*args, **kwargs)
    '''
    def save(self, *args, **kwargs):
        if not self.pk:
        # This code only happens if the objects is
        # not in the database yet. Otherwise it would
        # have pk
        super(MyModel, self).save(*args, **kwargs)
    '''



