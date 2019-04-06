from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^subjectpart/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^subjectpart/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^subjectpart/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^subjectpart/create$', views.create, name='create'),
    url(r'^ajax/validate_subjectsubjectpart/$', views.validate_subjectsubjectpart, name="validate_subjectsubjectpart"),
]