from django.conf.urls import url

# from . import is a relative import
# it will look in the analysis folder and find views.py from there
from . views import analysisList, analysisDetail
urlpatterns = [
    url(r'^$',analysisList.as_view(), name='analysis'),
    url(r'^analyze/(?P<pk>[0-9]+)/$', analysisDetail.as_view(), name='analyze'),
]