from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from . models import Project
from . forms import ProjectForm


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():

            newdoc = Project(source=request.FILES['projectFile'], name=form['name'].value(), extension=form['extension'].value())
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

from django.shortcuts import get_object_or_404

def delete(request):
    print('step 1')
    docId = request.POST.get('deletethis', None)
    print(docId)
    docToDel = get_object_or_404(Project, pk = docId)
    print(docToDel)
    docToDel.source.delete()
    print('deleting')
    docToDel.delete()

    return HttpResponseRedirect(reverse('projects'))