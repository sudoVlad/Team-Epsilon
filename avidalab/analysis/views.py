from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
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

        #Here is where we could get the list of runs form the project
        # For proof of concept right now the runs are just a list of 1 2 3
        context['runs'] = ['1', '2', '3']
        # and the data files are just A B C
        context['data_files'] = ['A', 'B', 'C']

        #Look at analysisDetail.html to see how to access the items in the list
        return context