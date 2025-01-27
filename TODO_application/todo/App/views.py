from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from App import models
from .models import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        email_id = request.POST.get('email')
        pwd = request.POST.get('pwd')
        print(fnm, email_id, pwd)
        my_user = User.objects.create_user(fnm, email_id, pwd)
        my_user.save()
        return redirect('/login')

    return render(request, 'signup.html')

def loginUser(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        print(fnm, pwd)
        us = authenticate(request, username = fnm, password = pwd)
        if us is not None:
            login(request, us)
            return redirect('/todopage')
        else:
            return redirect('login/')
    return render(request, 'login.html')

def todopage(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        print(title)
        obj=App(title=title,user=request.user)
        obj.save()
        user=request.user
        res=App.objects.filter(user=request.user).order_by('-date')
        return redirect('/todopage',{'res':res})
    res=App.objects.filter(user=request.user).order_by('-date')
    return render(request,"todo.html",{'res':res})


def edit_todo(request,srno):
    if request.method == 'POST':
        title=request.POST.get('title')
        print(title)
        obj=App.objects.get(srno=srno)
        obj.title=title
        obj.save()
        user=request.user
        res=App.objects.filter(user=request.user).order_by('-date')
        return redirect('/todopage',{'obj':obj})
    obj=App.objects.get(srno=srno)
    res=App.objects.filter(user=request.user).order_by('-date')
    return render(request,"edit_todo.html",{'res':obj})


def delete_todo(request,srno):
    obj=App.objects.get(srno=srno)
    obj.delete()
    return redirect('/todopage')

def signout(request):
    logout(request)
    return redirect('/login')