from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView

# Create your views here.
#function based view
# def home(request):
#     return render(request,'book.html')


#class based view
class MyTemplateView(TemplateView):
    template_name='book/home.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context = {'name':'sefat','age':21}
        context.update(kwargs)
        return context
    

# def bookStore(request):
#     if request.method == 'POST':
#        book = BookStoreForm(request.POST)
#        if book.is_valid():
#            book.save()
#            return redirect('showbook')
#     else:
#         book = BookStoreForm()
#     return render(request,'book/store_book.html',{'book':book})


# class BookFormView(FormView):
#     template_name = 'book/store_book.html'
#     form_class = BookStoreForm
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         form.save()
#         return redirect('showbook')
        

class BookFormView(CreateView):
    model = BookStoreModel
    template_name = 'book/store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('showbook')
    
    
    


# def show_book(request):
#    book = BookStoreModel.objects.all()
#    return render(request,'book/show_book.html',{'form':book}) 

#class based view
class BookListView(ListView):
    model = BookStoreModel
    template_name = 'book/show_book.html'
    context_object_name = 'form'
    # def get_queryset(self):
    #     return BookStoreModel.objects.filter(id='2')
    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     context = {'sefat' : BookStoreModel.objects.all().order_by('author')}
    #     return context
    #ordering = ['-id']
    # def get_template_names(self) : #template ka override korbo
    #     if self.request.user.is_superuser:
    #         template_name = ''
    #     elif self.request.user.is_staff:
    #         template_name = ''
    #     else:
    #         template_name = ''
    #     return [template_name]
    
    
    
class BookDetailsView(DetailView):
    model = BookStoreModel
    template_name = 'book/book_details.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'

# def edit_book(request,id):
#     book = BookStoreModel.objects.get(pk = id)
#     form = BookStoreForm(instance=book)
#     if request.method == 'POST':
#        form = BookStoreForm(request.POST,instance=book)
#        if form.is_valid():
#            form.save()
#            return redirect('showbook')
#     return render(request,'book/store_book.html',{'book':form})

# def delete_book(request,id):
#     book = BookStoreModel.objects.get(pk = id).delete()
#     return redirect('showbook')
    
class BookUpadteView(UpdateView):
    model = BookStoreModel
    template_name = 'book/store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('showbook')

class BookDeleteView(DeleteView):
    model = BookStoreModel
    template_name = 'book/delete_confarmation.html'
    success_url = reverse_lazy('showbook')
    