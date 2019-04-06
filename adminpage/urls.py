from django.urls import path
from . import views

app_name = 'adminpage'

urlpatterns = [
    path('admin1/', views.admin1, name = 'admin1'),
    path('admin2/', views.admin2, name = 'admin2'),
    # path('tables_object/', views.tables_object, name = 'tables_object'),
    # path('tables_relationship/', views.tables_relationship, name = 'tables_relationship'),
    # path('tables_SEO/', views.tables_SEO, name = 'tables_SEO'),
]