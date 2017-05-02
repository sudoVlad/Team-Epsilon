from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView , DeleteView, ListView, CreateView
from django.shortcuts import get_object_or_404
from . models import Project
from . forms import ProjectForm
from . unzip import unzip_project

class edit(UpdateView):
    model = Project
    fields = '__all__'
    template_name = "projectedit.html"

    def get_success_url(self):
        return reverse_lazy('projects')


class delete(DeleteView):
    model = Project
    fields = '__all__'
    template_name = "projectdel.html"

    def get_success_url(self):
        return reverse_lazy('projects')

class listProjects(ListView):
    model = Project
    fields = '__all__'
    template_name = 'projectlist.html'

'''
class createProjects(CreateView):
    #form_class = ProjectForm
    model = Project
    fields = ['name', 'source']
    template_name = 'projectcreate.html'

    def get_success_url(self):
        return reverse_lazy('projects')
'''

def unzip(request, pk):
    print('in the view')
    #we should be passed the project ID as data from the form ont he previous page
    unzip_project(Project.objects.get(id=pk))
    #we should call the unzip function on the source of the project grabbed from the ID

    #we should then update the decompressed field on the project to be the directory of the unzipped files


    return HttpResponseRedirect(reverse('projects'))

def list(request):
    # Handle file upload
    if request.method == 'POST':
        #print(request.POST)
        #print(request.FILES)
        form = ProjectForm(request.POST, request.FILES)
        #print('======**=========')
        #print(form)
        #print('======**=========')
        if form.is_valid():

            newdoc = Project(source=request.FILES['projectFile'], name=form['name'].value(), decompressed='COMPRESSED')
            newdoc.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('projects'))
    else:
        form = ProjectForm()  # A empty, unbound form

    # Load documents for the list page
    projects = Project.objects.all()
    #print("These are the projects==========!")
    #print(projects)
    # Render list page with the documents and the form
    return render(
        request,
        'project.html',
        {'projects': projects, 'form': form}
    )

