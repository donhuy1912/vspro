from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^tables_relationship/$', views.index, name='index'),
    url(r'^subjectteacher/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^subjectteacher/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^subjectteacher/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^subjectteacher/create$', views.create, name='create'),
]
