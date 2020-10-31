from .models import *
from datetime import datetime

def checkUserNameExist(username):
    data = Register.objects.filter(username=username)

    return True if len(data) > 0 else False

def updateLoginTime(object):
    login_time = datetime.timestamp(datetime.now())
    stats = LoginStats(user=object, login_time=login_time)
    stats.save()
    return None