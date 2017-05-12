from django.conf.urls import url

# from . import is a relative import
# it will look in the analysis folder and find views.py from there
from . views import analysisList, analysisRunDetail, analysisExpDetail, analysisFieldDetail
urlpatterns = [
    url(r'^$',analysisList.as_view(), name='analysis'),
    #url(r'^analyze/(?P<pk>[0-9]+)/$', analysisDetail.as_view(), name='analyze'),
    url(r'^analyzeExp/(?P<pk>[0-9]+)/$', analysisExpDetail.as_view(), name='analyze'),
    url(r'^analyzeRun/$', analysisRunDetail, name='analyzeRun'),
    url(r'^analysisField/$', analysisFieldDetail, name='analysisField'),
]