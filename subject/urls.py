from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^subject/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^subject/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^subject/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^subject/create$', views.create, name='create'),
]