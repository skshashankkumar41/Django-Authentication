from .models import *
from datetime import datetime
import requests

def checkUserNameExist(username):
    data = Register.objects.filter(username=username)

    return True if len(data) > 0 else False

def updateLoginTime(object):
    login_time = datetime.timestamp(datetime.utcnow())
    stats = LoginStats(user=object, login_time=login_time)
    stats.save()
    return None

def getLastLogin(object):
    try:
        lastLogin = object.order_by('-login_time')[1].login_time
    except:
        lastLogin = object.order_by('-login_time').first().login_time

    return lastLogin

def getIpLocation():
    data = requests.get('http://ipinfo.io/json/?token=4ded5bd112c5ba').json()

    return {
        'city': data.get('city'),
        "state": data.get('region'),
        "country": data.get('country'),
        "timezone": data.get('timezone'),
        "org": data.get('org')
    }