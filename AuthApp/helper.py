from .models import *
from datetime import datetime

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
        lastLogin = login_data.order_by('-login_time')[1].login_time
    except:
        lastLogin = login_data.order_by('-login_time').first().login_time

    return lastLogin