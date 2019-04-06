from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^sliderunbar/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^sliderunbar/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^sliderunbar/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^sliderunbar/create$', views.create, name='create'),
]