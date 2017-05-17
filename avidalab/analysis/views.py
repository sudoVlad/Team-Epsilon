from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from os import listdir
from os import walk
from django.views.generic import UpdateView , DeleteView, ListView, CreateView, DetailView
from projects.models import Project
from projects.ParsingData import parseFile, mapData
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

#To use graph functions
from graphData import *

import json
import numpy as np

# mean array maker takes an array of arrays and creates an array that contains the mean array as defined below
# [1, 2, 3], [4, 5, 6], [7, 8, 9]
# the result would be [6, 7.5, 9]
#
def mean_array_maker(arrays):
    result = []
    if len(arrays) == 0:
        return result

    min_size = len(arrays[0])

    #grab the min size to make all arrays the same size
    for array in arrays:
        min_size = min(min_size, len(array))
    # make all arrays the same size
    for array in arrays:
        result.append(array[:min_size])

    #do the mean array stuff
    np_arrays = np.array(result)
    mean_array = np_arrays.mean(axis=0)
    return mean_array

# Create your views here.
#def index(request):
#    template = loader.get_template('analysis/analysis_index.html')
#    return HttpResponse(template.render(request))

class analysisList(ListView):
    model = Project
    template_name = 'analysisList.html'
    fields ='__all__'
'''
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
'''

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
                if name not in dataFiles:
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
    if not runs:
        return HttpResponseRedirect(reverse('analysis'))
    data = request.GET.get('selectedData')
    ##got to generate the list of fields to pick from
    fields = parseFile(Project.objects.get(id=projectID).decompressed + '//' + exp + '//' + runs[0] + '//' + data)

    print(runs)


    return render(request,
                  'analysisFieldDetail.html',
                  {'exp':exp,
                   'projectID':projectID,
                   'runs':runs,
                   'data':data,
                   'fields':fields
                   }
                  )

def analysisGraphs(request):

    ##lets go ahead and start getting dictionaries from each for the runs
    runs = request.GET.getlist('newRuns')
    field = request.GET.get('selectedField')
    exp = request.GET.get('exp')
    data = request.GET.get('data')
    projectID = request.GET.get('projectID')
    project = Project.objects.get(id=projectID)
    path = project.decompressed

    all_the_dictionaries = []
    print(runs)
    for run in runs:
        #start by getting the full path to the file
        full_path = path + '//' + exp + '//' + run + '//' + data
        print(run)
        #then we get map data from the function
        all_the_dictionaries.append(mapData(full_path))


    ##Get an array of graph images!
    graphs = []



    return render(request,
                  'analysisGraphs.html',
                  {'test':'test',
                   'dictionarys':all_the_dictionaries,
                   'graphs':graphs
                   }
                  )

def analysisStats(request):

    ##lets go ahead and start getting dictionaries from each for the runs
    runs = request.GET.getlist('newRuns')
    field = request.GET.get('selectedField')
    exp = request.GET.get('exp')
    data = request.GET.get('data')
    projectID = request.GET.get('projectID')
    project = Project.objects.get(id=projectID)
    path = project.decompressed

    all_the_dictionaries = []
    print(runs)
    for run in runs:
        #start by getting the full path to the file
        full_path = path + '//' + exp + '//' + run + '//' + data
        print(run)
        #then we get map data from the function
        all_the_dictionaries.append(mapData(full_path))


    ##Get an array of stats values!
    stats = []



    return render(request,
                  'analysisStats.html',
                  {'test':'test',
                   'dictionarys':all_the_dictionaries,
                   'stats':stats
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
