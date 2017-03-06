from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$import/', views.index, name='index'),
]
