from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^subjectlike/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^subjectlike/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^subjectlike/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^subjectlike/create$', views.create, name='create'),
]
