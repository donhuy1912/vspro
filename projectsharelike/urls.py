from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^projectsharelike/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^projectsharelike/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^projectsharelike/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^projectsharelike/create$', views.create, name='create'),
]
