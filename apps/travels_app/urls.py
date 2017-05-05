from django.conf.urls import url
from . import views

app_name = 'travel'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^add$', views.add, name='add'),
    url(r'^destination/(?P<id>\d+)$', views.destination, name='destination'),
    url(r'^join/(?P<id>\d+)$', views.join, name='join'),
    url(r'^logout$', views.logout, name='logout'),

]
