from django.conf.urls import url
from . views import list
from . views import delete
from . views import edit

urlpatterns = [
    url(r'^$', list, name='projects'),
    url(r'^delete/', delete, name='delete'),
    url(r'^edit/', edit.as_view(), name='edit'),

]