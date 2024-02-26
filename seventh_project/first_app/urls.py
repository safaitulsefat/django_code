from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('',views.show_data,name='homepage'),
]
