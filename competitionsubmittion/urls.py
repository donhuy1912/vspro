from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^competitionsubmittion/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^competitionsubmittion/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^competitionsubmittion/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^competitionsubmittion/create$', views.create, name='create'),
    url(r'^ajax/validate_subjectcompetitionsubmittion/$', views.validate_subjectcompetitionsubmittion, name='validate_subjectcompetitionsubmittion'),
    url(r'^ajax/validate_subjectpartcompetitionsubmittion/$', views.validate_subjectpartcompetitionsubmittion, name='validate_subjectpartcompetitionsubmittion')
]