from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .helper import *
from datetime import datetime
import pytz
# Create your views here.

def landing(request):
    return render(request,'landing.html')

def signup(request):
    return render(request,'signup.html')

def logout(request):
    username = request.session.get('username')
    login_data = LoginStats.objects.filter(user=username).order_by('-login_time').first()
    login_data.logout_time = datetime.timestamp(datetime.utcnow())
    login_data.save()
    del request.session['username']
    return redirect('home')

def renderDashboard(request):
    tz = pytz.timezone('Asia/Kolkata')
    username = request.session.get('username')
    user_data = Register.objects.filter(username=username)
    login_data = LoginStats.objects.filter(user=username)
    loginCounts = len(login_data)
    lastLogin = getLastLogin(login_data)
    lastLogin = pytz.utc.localize(datetime.fromtimestamp(lastLogin)).astimezone(tz).strftime("%d/%m/%Y, %H:%M:%S")
    userCreated = pytz.utc.localize(datetime.fromtimestamp(user_data.first().date_created)).astimezone(tz).strftime("%d/%m/%Y, %H:%M:%S")
    
    return render(request,'dashboard.html',{'username':username,'login_counts':loginCounts,'last_login':lastLogin,'user_created':userCreated})

def register(request):
    name = request.POST['name']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    mobile = request.POST['mobile']
    date_created = datetime.timestamp(datetime.utcnow())
    ipData = getIpLocation()

    if not checkUserNameExist(username):
        reg = Register(name=name,email=email,username=username,password=password,mobile=mobile,date_created=date_created,city=ipData['city'],country=ipData['country'],state=ipData['state'],timezone=ipData['timezone'],org=ipData['org'])
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
            request.session['username'] = data.first().username
            return redirect("dashboard")

        else:
            return render(request,'landing.html',{'tag':'Incorrect Password'})

    return render(request,'landing.html',{'tag':'Username doesn\'t exists'})

