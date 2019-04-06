from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^news/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^news/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^news/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^news/create$', views.create, name='create'),
    url(r'^ajax/validate_subjectnews/$', views.validate_subjectnews, name='validate_subjectnews')
]