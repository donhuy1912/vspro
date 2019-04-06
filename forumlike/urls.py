from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^forumlike/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^forumlike/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^forumlike/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^forumlike/create$', views.create, name='create'),
]
