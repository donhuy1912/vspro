from django.conf.urls import url
from . import views

urlpatterns= [
    # url(r'^$', views.index, name='index'),
    url(r'^activity/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^activity/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^activity/edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^activity/create$', views.create, name='create'),

    url(r'^ajax/validate_subjectactivity/$', views.validate_subjectactivity, name="validate_subjectactivity"),
    url(r'^ajax/validate_chapteractivity/$', views.validate_chapteractivity, name="validate_chapteractivity"),
    url(r'^ajax/validate_lessonactivity/$', views.validate_lessonactivity, name="validate_lessonactivity"),
    url(r'^ajax/validate_lessonactivityactivity/$', views.validate_lessonactivityactivity, name="validate_lessonactivityactivity"),
    url(r'^ajax/validate_itemorderactivity/$', views.validate_itemorderactivity, name="validate_itemorderactivity"),
]