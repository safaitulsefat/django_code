
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='homepage'),
    path('bookstore/',views.bookStore,name='bookstore'),
    path('showbook/',views.show_book,name='showbook'),
    path('editbook/<int:id>',views.edit_book,name='editbook'),
    path('deletebook/<int:id>',views.delete_book,name='deletebook')
]
