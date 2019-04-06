from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^forumreply/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^forumreply/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^forumreply/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^forumreply/create$', views.create, name='create'),
]
