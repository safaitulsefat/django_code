from django.shortcuts import render
from django.http import HttpResponse
from . forms import contact_form,student,PasswordValidationProject
# Create your views here.
def Home(request):
    
    return render(request,'./first_app/home.html',{"name" : "I am Rahim", "marks" : 86, "lst" : [24,3,10,5], "blog" : "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Harum quae tempora fugit laborum voluptas mollitia. Explicabo earum assumenda obcaecati et.","courses" : [
        {
        "id" : 1,
        "course" : "C",
        "teacher" : "Rahim"
        },
        {
        "id" : 2,
        "course" : "C++",
        "teacher" : "Kahim"
        },
        {
        "id" : 3,
        "course" : "Python",
        "teacher" : "Fahim"
        },
        ]})
    
def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request,'./first_app/about.html',{'name':name,'email':email,'select':select})
    else:
         return render(request,'./first_app/about.html')
def show_form(request):
    return render(request,'./first_app/forms.html')

def django_form(request):
    if request.method == 'POST':
        form = contact_form(request.POST, request.FILES)
        if form.is_valid():
          file = form.cleaned_data['file']
          with open('./first_app/upload/' + file.name, 'wb+') as destination:
              for chunk in file.chunks():
                  destination.write(chunk)
          print(form.cleaned_data)
          return render(request,'./first_app/django_form.html',{'form':form})
    else:
        form = contact_form()
    return render(request,'./first_app/django_form.html',{'form':form})

def student_form(request):
    if request.method == 'POST':
        form = student(request.POST, request.FILES)
        if form.is_valid():
          print(form.cleaned_data)
          
    else:
        form = student()
    return render(request,'./first_app/django_form.html',{'form':form})

def passwordValidator(request):
    if request.method == 'POST':
        form = PasswordValidationProject(request.POST)
        if form.is_valid():
          print(form.cleaned_data)
          
    else:
        form = PasswordValidationProject()
    return render(request,'./first_app/django_form.html',{'form':form})