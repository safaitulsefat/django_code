from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.home,name='homepage'),
    path('signup/',views.sign_up,name='signuppage'),
    path('login/',views.user_login,name='loginpage'),
    path('profile/',views.user_profile,name='profilepage'),
    path('logout/',views.user_logout,name='logoutpage'),
    path('passwordchange/',views.pass_change,name='passwordchange'),
    path('passwordchange2/',views.pass_change2,name='passwordchange2')
]