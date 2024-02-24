from django.shortcuts import render,redirect
from . import models
# Create your views here.
def home(request):
    student = models.studen.objects.all()
    return render(request,'index.html',{'data':student})

def delete_student(request,roll):
    std = models.studen.objects.get(pk=roll).delete()
    return redirect('homepage')