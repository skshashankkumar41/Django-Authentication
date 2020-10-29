from .models import Register

def checkUserNameExist(username):
    data = Register.objects.filter(username=username)

    return True if len(data) > 0 else False