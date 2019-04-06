from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^lesson/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^lesson/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^lesson/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^lesson/create$', views.create, name='create'),
    url(r'^ajax/validate_subjectlesson/$', views.validate_subjectlesson, name='validate_subjectlesson'),
    url(r'^ajax/validate_subjectorderlesson/$', views.validate_subjectorderlesson, name='validate_subjectorderlesson'),
    url(r'^ajax/validate_chapterorderlesson/$', views.validate_chapterorderlesson, name='validate_chapterorderlesson'),
]