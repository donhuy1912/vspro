from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^header/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^header/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^header/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^header/create$', views.create, name='create'),
]