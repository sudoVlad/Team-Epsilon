from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView , DeleteView, ListView, CreateView
from django.shortcuts import get_object_or_404
from . models import Project
from . forms import ProjectForm


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

from zipfile import ZipFile
import os
FULLPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def unpack_zip(zipfile='', path_from_local='', remove=False):
    print(zipfile + ' '+ path_from_local)
    filepath = path_from_local + zipfile
    extract_path = path_from_local
    parent_archive = ZipFile(filepath)
    parent_archive.extractall(extract_path)
    namelist = parent_archive.namelist()
    parent_archive.close()
    for name in namelist:
        try:
            unpack_zip(zipfile=name.split('/')[1], path_from_local=filepath.strip('.zip') + '\\', remove=True)

        except:
            continue

    if remove:
        os.remove(filepath)
    return filepath.strip('.zip')

def unzip(request, pk):
    print('in the view')
    #grab the source files name
    project = Project.objects.get(id=pk)
    source_url = project.source.url
    source_name = project.source.name

    print('=====')
    print(FULLPATH)
    source_name = os.path.basename(source_url)
    print(source_name)
    source_url = FULLPATH + '/' + source_url.split(source_name)[0]
    print(source_url)
    print('=====')
    decpath = unpack_zip(zipfile=source_name,path_from_local=source_url)
    project.decompressed = decpath
    project.save()
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

