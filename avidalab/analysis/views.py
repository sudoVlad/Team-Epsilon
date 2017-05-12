from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from os import listdir
from os import walk
from django.views.generic import UpdateView , DeleteView, ListView, CreateView, DetailView
from projects.models import Project



# Create your views here.
#def index(request):
#    template = loader.get_template('analysis/analysis_index.html')
#    return HttpResponse(template.render(request))

class analysisList(ListView):
    model = Project
    template_name = 'analysisList.html'
    fields ='__all__'

class analysisDetail(DetailView):
    model = Project
    template_name = 'analysisDetail.html'
    fields = '__all__'



    #So before we go into the view we want to make sure we pass enough data to it!
    # This can be done by adding a new entry into the context array and assigning it values

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(analysisDetail, self).get_context_data(**kwargs)
        context['runs'] = listdir(context['project'].decompressed)
        # go through the directory at decompressed
        # and pull out any files that end with .dat
        tempList = []
        # should be in the selected runs only
        #selectedRuns= ['run_1']
        # but right now goes through all of decompressed's files
        for path, subdirs, files in walk(context['project'].decompressed):
            for name in files:
                path.join(name)
                if(name.endswith('.dat')):
                    tempList.append(name)
        context['data_files'] = tempList

        #Look at analysisDetail.html to see how to access the items in the list
        return context


def analysisRunDetail(request):
    #now we need some data to pass yay
    exp = request.GET.get('exp')
    projectID = request.GET.get('projectID')

    ##now we build the runs array
    project = Project.objects.get(id=projectID)

    runs = listdir(project.decompressed + '//' + exp)

    ##now get the data files

    dataFiles = []
    # should be in the selected runs only
    # selectedRuns= ['run_1']
    # but right now goes through all of decompressed's files
    for path, subdirs, files in walk(project.decompressed):
        for name in files:
            path.join(name)
            if (name.endswith('.dat')):
                dataFiles.append(name)

    return render(request,
                  'analysisRunDetail.html',
                  {'exp':exp,
                   'projectID':projectID,
                   'runs':runs,
                   'dataFiles':dataFiles
                   }
                  )

def analysisFieldDetail(request):
    #get the hidden data
    exp = request.GET.get('exp')
    projectID = request.GET.get('projectID')

    runs = request.GET.getlist('selectedRuns')

    print(runs)
    data = request.GET.get('selectedData')

    return render(request,
                  'analysisFieldDetail.html',
                  {'exp':exp,
                   'projectID':projectID,
                   'runs':runs,
                   'data':data
                   }
                  )


class analysisExpDetail(DetailView):
    model = Project
    template_name = 'analysisExpDetail.html'
    fields = '__all__'



    #So before we go into the view we want to make sure we pass enough data to it!
    # This can be done by adding a new entry into the context array and assigning it values

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(analysisExpDetail, self).get_context_data(**kwargs)

        context['exps'] = listdir(context['project'].decompressed)


        #Look at analysisDetail.html to see how to access the items in the list
        return context