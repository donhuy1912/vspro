from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^projectsharereply/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^projectsharereply/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^projectsharereply/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^projectsharereply/create$', views.create, name='create'),
]
