from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^enviromentcate/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^enviromentcate/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^enviromentcate/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^enviromentcate/create$', views.create, name='create'),
]