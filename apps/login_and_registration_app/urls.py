from django.conf.urls import url
from . import views

app_name = 'auth'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registration$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
]
