from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='homepage'),
    path('showtask/',views.show_task,name='showpage'),
    path('edittask/<int:id>',views.edit_task,name='edittask'),
    path('deletetask/<int:id>',views.delete_task,name='deletetask'),
    path('completed/<int:id>',views.complete,name='completed'),
    path('completedtask/',views.completed_task,name='completedtask')
]
