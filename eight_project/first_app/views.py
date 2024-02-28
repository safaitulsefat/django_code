from django.shortcuts import render,redirect

from .forms import RegistationForm,ChangeUserData
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
# Create your views here.
def home(request):
    return render(request,'./home.html')
def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
          form = RegistationForm(request.POST)
          if form.is_valid():
            messages.success(request,'account created succesfully')
            form.save()
            print(form.cleaned_data)
        else:
            form = RegistationForm()
        return render(request,'./signup.html',{'form':form})
    else:
        return redirect('profilepage')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name,password=userpass)
                if user is not None:
                    login(request,user)
                    return redirect('profilepage')
        else:
            form = AuthenticationForm()
        return render(request,'./login.html',{'form':form})
    else:
        return redirect('profilepage')

def user_profile(request):
    if  request.user.is_authenticated:
        if request.method == 'POST':
          form = ChangeUserData(request.POST, instance=request.user)
          if form.is_valid():
            messages.success(request,'account updated succesfully')
            form.save()
            print(form.cleaned_data)
        else:
            form = ChangeUserData(instance=request.user)
        return render(request,'./profile.html',{'form':form})
    else:
        return redirect('signuppage')
def user_logout(request):
    logout(request)
    return redirect('loginpage')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data= request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profilepage')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'./passwordchange.html',{'form':form})
    else:
        return redirect("login")
    
def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user,data= request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profilepage')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request,'./passwordchange.html',{'form':form})
    else:
        return redirect("login")

def Change_User_Data(request):
    if  request.user.is_authenticated:
        if request.method == 'POST':
          form = ChangeUserData(request.POST, instance=request.user)
          if form.is_valid():
            messages.success(request,'account updated succesfully')
            form.save()
            print(form.cleaned_data)
        else:
            form = ChangeUserData()
        return render(request,'./profile.html',{'form':form})
    else:
        return redirect('signuppage')
