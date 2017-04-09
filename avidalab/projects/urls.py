from django.conf.urls import url
from . views import list
from . views import delete
from . views import edit

urlpatterns = [
    url(r'^$', list, name='projects'),
    url(r'^delete/(?P<pk>[0-9]+)/$', delete.as_view(), name='delete'),
    url(r'edit/(?P<pk>[0-9]+)/$', edit.as_view(), name='edit'),

]