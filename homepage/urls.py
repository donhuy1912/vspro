from django.urls import path
from . import views
from django.conf.urls import url


app_name = 'homepage'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.myLogin, name = 'login'),
    path('logout/', views.myLogout, name = 'logout'),
    path('register/', views.myRegister, name = 'register'),
    
    
    path('introduction/', views.introduction, name = 'introduction' ),
    path('aboutus/', views.aboutUs, name = 'aboutus'),
	path('vision/', views.vision, name = 'vision'),
	path('team/', views.team, name = 'team'),
    path('myprofile/<int:id>/', views.myProfile, name = 'myprofile' ), 
	path('myprofile/<int:id>/changepassword/', views.myChangepassword, name = 'changepassword'),
    path('forgotpassword/', views.passForgot, name = 'forgotpass'),
    path('confirmpassword/', views.passConfirm, name = 'confirmpass'),
    path('activeaccount/', views.activeAccount, name = 'activeaccount'),
    path('confirmaccount/', views.confirmAccount, name =  'confirmaccount'),

    path('userprofile/<int:idguest>/', views.userprofile, name="userprofile"),
    path('search/<str:subname>', views.searchsub, name="search"),
        
    # path('myprofile/<int:id>/', views.myProfile, name = 'myprofile' ),
    path('editprofile/<int:id>/', views.editMyProfile, name = 'editmyprofile' ),

    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    # url(r'^ajax/validate_email/$', views.validate_email, name='validate_email')

 
]