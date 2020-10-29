from django.shortcuts import render, redirect
from .models import Register
from .helper import *
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

    if not checkUserNameExist(username):
        reg = Register(name=name,email=email,username=username,password=password,mobile=mobile)
        reg.save()
        return render(request,'landing.html')

    else:
        return render(request,'landing.html')

    

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    data = Register.objects.filter(username=username)

    if len(data) > 0:
        if data[0].password == password:
            return redirect("https://skshashankkumar41.github.io/")

    return render(request,'landing.html')