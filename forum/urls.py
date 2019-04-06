from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^forum/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^forum/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^forum/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^forum/create$', views.create, name='create'),
    url(r'ajax/validate_subjectforum/$', views.validate_subjectforum, name="validate_subjectforum")
]