from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^chapter/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^chapter/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^chapter/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^chapter/create$', views.create, name='create'),
    url(r'^ajax/validate_subjectorderchapter/$', views.validate_subjectorderchapter, name="validate_subjectorderchapter"),
]