from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^activitytype/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^activitytype/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^activitytype/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^activitytype/create$', views.create, name='create'),
]