from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^competitionsubmittionreply/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^competitionsubmittionreply/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^competitionsubmittionreply/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^competitionsubmittionreply/create$', views.create, name='create'),
    url(r'ajax/validate_competitioncompetitionsubmittionreply/$', views.validate_competitioncompetitionsubmittionreply, name='validate_competitioncompetitionsubmittionreply'),
]
