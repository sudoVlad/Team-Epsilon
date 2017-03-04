from django.conf.urls import url
# from . import is a relative import
# it will look in the analysis folder and find views.py from there
from . import views
urlpatterns = [
    url(r'^$',views.index, name='analysis'),
]