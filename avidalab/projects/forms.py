from django import forms
from . models import Project
from django.core.exceptions import ValidationError

def validate_file_extension(value):

    if not value.name.endswith('.tar.gz'):
        raise ValidationError(u'Only Appropriate compressed files allowed')

class ProjectForm(forms.Form):
    class Meta:
        model = Project
        fields = '__all__'

    projectFile = forms.FileField(
        label='Select a file',
        validators=[validate_file_extension]
    )

    name = forms.CharField(required=True)


