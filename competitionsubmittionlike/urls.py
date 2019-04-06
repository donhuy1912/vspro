from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^competitionsubmittionlike/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^competitionsubmittionlike/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^competitionsubmittionlike/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^competitionsubmittionlike/create$', views.create, name='create'),
    url(r'ajax/validate_competitioncompetitionsubmittionlike/$', views.validate_competitioncompetitionsubmittionlike, name='validate_competitioncompetitionsubmittionlike'),
]
