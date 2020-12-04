from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"Account created successfully for " + user)
            return redirect('/accounts/login')
    context = {'form':form}
    return render(request,'accounts/signup.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is inccorrect')
            

    context = {}
    return render(request, 'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')