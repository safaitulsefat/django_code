from django.http import HttpResponse
from django.shortcuts import redirect, render
from task.forms import taskForm
from task.models import TaskModel

# def home(request):
#     if request.user.is_authenticated:
#         user_id = request.user.id
#     if request.method == 'POST':
#         task = taskForm(request.POST)
#         if task.is_valid():
#             task.save()
#     else:  
#         task = taskForm()
#     return render(request,'task/home.html',{'task':task})



def home(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        if request.method == 'POST':
            task = taskForm(request.POST)
            if task.is_valid():
                task_instance = task.save(commit=False)   
                task_instance.user_id = user_id  
                task_instance.save()  
        else:  
            task = taskForm()
        return render(request, 'task/home.html', {'task': task})
    else:
        return HttpResponse("You need to be logged in to access this page.")


def show_task(request):
   
    if request.user.is_authenticated:
        user_id = request.user.id
    show = TaskModel.objects.filter(user_id=user_id)
    return render(request,'task/show.html',{'show':show})

def edit_task(request,id):
    task = TaskModel.objects.get(pk =id)
    form = taskForm(instance=task)
    if request.method == 'POST':
        form = taskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('showpage')
    return render(request,'task/home.html',{'task':form})

def delete_task(request,id):
    task = TaskModel.objects.get(pk=id).delete()
    return redirect('showpage')

def complete(request,id):
    task = TaskModel.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('showpage')

def completed_task(request):
    if request.user.is_authenticated:
        user_id = request.user.id
    comte = TaskModel.objects.filter( user_id= user_id)
    return render(request,'task/complete.html',{'show':comte})

    