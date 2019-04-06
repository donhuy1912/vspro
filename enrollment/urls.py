from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^tables_relationship/$', views.index, name='index'),
    url(r'^enrollment/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^enrollment/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^enrollment/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^enrollment/create$', views.create, name='create'),
]
