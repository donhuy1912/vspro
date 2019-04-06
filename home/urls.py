from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^home/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^home/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^home/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^home/create$', views.create, name='create'),
]