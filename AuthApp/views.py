from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .helper import *
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from datetime import datetime
# Create your views here.

def landing(request):
    return render(request,'landing.html')

def signup(request):
    return render(request,'signup.html')

def register(request):
    name = request.POST['name']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    mobile = request.POST['mobile']
    date_created = datetime.timestamp(datetime.now())

    if not checkUserNameExist(username):
        reg = Register(name=name,email=email,username=username,password=password,mobile=mobile,date_created=date_created)
        reg.save()
        return redirect('home')

    else:
        return render(request,'signup.html',{'tag':'Username already Exists'})

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    data = Register.objects.filter(username=username)

    if len(data) > 0:
        if data.first().password == password:
            updateLoginTime(data.first())
            return redirect("https://skshashankkumar41.github.io/")

        else:
            return render(request,'landing.html',{'tag':'Incorrect Password'})

    return render(request,'landing.html',{'tag':'Username doesn\'t exists'})

