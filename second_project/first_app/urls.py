
from . import views
from django.urls import include, path

urlpatterns = [
    path('about/',views.about),
    path('contact/',views.contact)
    
]
