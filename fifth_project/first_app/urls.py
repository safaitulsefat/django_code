
from . import views

from django.urls import  path

urlpatterns = [
    path('',views.Home,name='home'),
    path('about/',views.about,name='about'),
    path('form/',views.show_form,name='form'),
    #path('django_form/',views.django_form,name='django_form'),
    path('django_form/',views.passwordValidator,name='django_form')

]
