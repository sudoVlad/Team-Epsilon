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
