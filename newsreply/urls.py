from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^newsreply/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^newsreply/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^newsreply/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^newsreply/create$', views.create, name='create'),
]
