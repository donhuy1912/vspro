from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^tracking/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^tracking/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^tracking/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^tracking/create$', views.create, name='create'),
    url(r'ajax/validate_subjecttracking/$', views.validate_subjecttracking, name='validate_subjecttracking'),
    url(r'ajax/validate_subjectparttracking/$', views.validate_subjectparttracking, name='validate_subjectparttracking'),
    url(r'ajax/validate_chaptertracking/$', views.validate_chaptertracking, name='validate_chaptertracking'),
    url(r'ajax/validate_lessontracking/$', views.validate_lessontracking, name='validate_lessontracking'),
    url(r'ajax/validate_itemtracking/$', views.validate_itemtracking, name='validate_itemtracking'),
]
