from django import forms

class ProjectForm(forms.Form):
    projectFile = forms.FileField(
        label='Select a file',
    )
    name = forms.CharField(required=True)
    extension = forms.CharField(required=True)