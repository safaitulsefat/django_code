from django.shortcuts import render
from first_app.forms import StudentForm
from first_app.models import teacher,student
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request,'first_app/home.html',{'form':form})

def show_data(request):
    #student list for 1 teacher
    teachers = teacher.objects.get(name = 'abul')
    studentss = teachers.students.all()
    for stud in studentss:
        print(stud.name,stud.roll,stud.class_name)
    #teacher list for 1 student
    studentss = student.objects.get(name = 'sefat')
    teachers = studentss.teacherss.all()
    for stud in teachers:
        print(stud.name,stud.subject,stud.mobile)
    return render(request,'first_app/show.html') 

    

