from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^activitysubmittion/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^activitysubmittion/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^activitysubmittion/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^activitysubmittion/create$', views.create, name='create'),
    url(r'ajax/validate_subjectactivitysubmittion/$', views.validate_subjectactivitysubmittion, name='validate_subjectactivitysubmittion'),
    url(r'ajax/validate_chapteractivitysubmittion/$', views.validate_chapteractivitysubmittion, name='validate_chapteractivitysubmittion'),
    url(r'ajax/validate_lessonactivitysubmittion/$', views.validate_lessonactivitysubmittion, name='validate_lessonactivitysubmittion'),
    url(r'ajax/validate_itemactivitysubmittion/$', views.validate_itemactivitysubmittion, name='validate_itemactivitysubmittion'),
]