from django.shortcuts import redirect, render
from book.forms import BookStoreForm
from book.models import BookStoreModel
# Create your views here.

def home(request):
    return render(request,'book/base.html')

def bookStore(request):
    if request.method == 'POST':
       book = BookStoreForm(request.POST)
       if book.is_valid():
           book.save()
    else:
        book = BookStoreForm()
    return render(request,'book/store_book.html',{'book':book})

def show_book(request):
   book = BookStoreModel.objects.all()
   return render(request,'book/show_book.html',{'form':book}) 

def edit_book(request,id):
    book = BookStoreModel.objects.get(pk = id)
    form = BookStoreForm(instance=book)
    if request.method == 'POST':
       form = BookStoreForm(request.POST,instance=book)
       if form.is_valid():
           form.save()
           return redirect('showbook')
    return render(request,'book/store_book.html',{'book':form})

def delete_book(request,id):
    book = BookStoreModel.objects.get(pk = id).delete()
    return redirect('showbook')
    