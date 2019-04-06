from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^activitysubmittionreply/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^activitysubmittionreply/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^activitysubmittionreply/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^activitysubmittionreply/create$', views.create, name='create'),
    url(r'ajax/validate_subjectactivitysubmittionreply/$', views.validate_subjectactivitysubmittionreply, name='validate_subjectactivitysubmittionreply'),
    url(r'ajax/validate_chapteractivitysubmittionreply/$', views.validate_chapteractivitysubmittionreply, name='validate_chapteractivitysubmittionreply'),
    url(r'ajax/validate_lessonactivitysubmittionreply/$', views.validate_lessonactivitysubmittionreply, name='validate_lessonactivitysubmittionreply'),
    url(r'ajax/validate_itemactivitysubmittionreply/$', views.validate_itemactivitysubmittionreply, name='validate_itemactivitysubmittionreply'),
    url(r'ajax/validate_activityactivitysubmittionreply/$', views.validate_activityactivitysubmittionreply, name='validate_activityactivitysubmittionreply'),
]