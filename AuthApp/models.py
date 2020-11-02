from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=200,null=True)
    username = models.CharField(primary_key=True, max_length=200)
    password = models.CharField(max_length=200,null=True)
    mobile = models.CharField(max_length=10,null=True)
    email = models.EmailField()
    city = models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    org = models.CharField(max_length=200,null=True)
    timezone = models.CharField(max_length=200,null=True)
    date_created = models.FloatField()

    def __str__(self):
        return self.username

class LoginStats(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    city = models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    timezone = models.CharField(max_length=200,null=True)
    org = models.CharField(max_length=200,null=True)
    login_time = models.FloatField(null=True)
    logout_time = models.FloatField(null=True)


    def __str__(self):
        return self.user.username

