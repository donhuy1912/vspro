from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^projectshare/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^projectshare/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^projectshare/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^projectshare/create$', views.create, name='create'),
    url(r'ajax/validate_subjectprojectshare/$', views.validate_subjectprojectshare, name='validate_subjectprojectshare')
]