from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^account/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^account/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^account/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^account/create$', views.create, name='create'),
]