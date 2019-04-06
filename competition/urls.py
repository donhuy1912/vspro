from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^competition/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^competition/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^competition/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^competition/create$', views.create, name='create'),
    url(r'ajax/validate_subjectcompetition/$', views.validate_subjectcompetition, name='validate_subjectcompetition')
]