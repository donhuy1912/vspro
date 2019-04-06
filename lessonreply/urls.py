from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^lessonreply/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^lessonreply/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^lessonreply/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^lessonreply/create$', views.create, name='create'),
    url(r'^ajax/validate_subjectlessonreply/$', views.validate_subjectlessonreply, name='validate_subjectlessonreply'),
    url(r'^ajax/validate_chapterlessonreply/$', views.validate_chapterlessonreply, name='validate_chapterlessonreply'),
]