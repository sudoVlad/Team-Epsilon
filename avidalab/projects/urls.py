from django.conf.urls import url
from . views import list
from . views import delete
from . views import edit
from . views import listProjects
#from . views import createProjects

urlpatterns = [
    url(r'^$', list, name='projects'),
    #url(r'^create/$', createProjects.as_view(), name='create'),
    url(r'^delete/(?P<pk>[0-9]+)/$', delete.as_view(), name='delete'),
    url(r'^edit/(?P<pk>[0-9]+)/$', edit.as_view(), name='edit'),

]