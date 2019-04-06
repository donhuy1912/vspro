from django.conf.urls import url
from . import views

urlpatterns= [
    # tables_SEO/
    url(r'^tables_SEO/$', views.index, name='index'),
    url(r'^introduction/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^introduction/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^introduction/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^introduction/create$', views.create, name='create'),
]