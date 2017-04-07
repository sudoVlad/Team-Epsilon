from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from . models import Project
from . forms import ProjectForm

class edit(UpdateView):
    model = Project
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_object(self):
        print(self.request.GET.get('editthis'))
        return Project.objects.get(pk=self.request.POST.get('editthis'))

    def get_success_url(self):
        return 'project/'

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():

            newdoc = Project(source=request.FILES['projectFile'], name=form['name'].value(), extension=form['extension'].value(), decompressed='COMPRESSED')
            newdoc.save()
            print(newdoc.name)
            print(newdoc.extension)
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('projects'))
    else:
        form = ProjectForm()  # A empty, unbound form

    # Load documents for the list page
    projects = Project.objects.all()
    print("These are the projects==========!")
    print(projects)
    # Render list page with the documents and the form
    return render(
        request,
        'project.html',
        {'projects': projects, 'form': form}
    )



def delete(request):
    #print('step 1')
    #the first thing you do is you do a get with post
    docId = request.POST.get('deletethis', None)
    #print(docId)
    #we then query the database for the object to delete
    docToDel = get_object_or_404(Project, pk = docId)
    #print(docToDel)
    #We then call the delete function on the file
    docToDel.source.delete()
    #print('deleting')
    #Then we call the delete function on the object in the database
    docToDel.delete()

    return HttpResponseRedirect(reverse('projects'))

