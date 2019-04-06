from django.conf.urls import url
from . import views
from django.urls import path
urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^item/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^item/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^item/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^item/create$', views.create, name='create'),

    
    url(r'^ajax/validate_subjectitem/$', views.validate_subjectitem, name='validate_subjectitem'),
    url(r'^ajax/validate_chapteritem/$', views.validate_chapteritem, name='validate_chapteritem'),
    url(r'^ajax/validate_lessonorderitem/$', views.validate_lessonorderitem, name='validate_lessonorderitem'),

]