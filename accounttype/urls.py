from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^accounttype/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^accounttype/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^accounttype/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^accounttype/create$', views.create, name='create'),
]