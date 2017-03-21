from django.conf.urls import url
from . views import list
from . views import delete

urlpatterns = [
    url(r'^$', list, name='projects'),
    url(r'^delete/', delete, name='delete'),
]