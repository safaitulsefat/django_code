
from . import views
from django.urls import path

urlpatterns = [
    #path('',views.home,name='homepage'),
    path('<int:roll>/',views.MyTemplateView.as_view(),{'author':'rahim'}),
    #path('bookstore/',views.bookStore,name='bookstore'),
    path('bookstore/',views.BookFormView.as_view(),name='bookstore'),
    #path('showbook/',views.show_book,name='showbook'),
    path('showbook/',views.BookListView.as_view(),name='showbook'),
    path('book_details/<int:id>',views.BookDetailsView.as_view(),name='book_details'),
    # path('editbook/<int:id>',views.edit_book,name='editbook'),
    # path('deletebook/<int:id>',views.delete_book,name='deletebook')
    path('editbook/<int:pk>',views.BookUpadteView.as_view(),name='editbook'),
    path('deletebook/<int:pk>',views.BookDeleteView.as_view(),name='deletebook')
]
