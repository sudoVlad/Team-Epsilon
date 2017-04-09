from django import forms
from . models import Project

class ProjectForm(forms.Form):
    class Meta:
        model = Project
        fields = '__all__'

    projectFile = forms.FileField(
        label='Select a file',
    )

    name = forms.CharField(required=True)
    extension = forms.ChoiceField(label=("With selected"), choices=(('none', '-----'),
                                                   ('targz', ('targz')),
                                                   ('none', ('none'))), required=True)


