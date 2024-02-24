from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',views.home,name='homepage'),
    path('delete/<int:roll>',views.delete_student,name='delete_student')
]