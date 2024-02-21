from . import views
from django.urls import include, path

urlpatterns = [
    path('course/',views.course),
    path('feedback/',views.feedback)
    
]