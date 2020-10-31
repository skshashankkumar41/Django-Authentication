from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=200,null=True)
    username = models.CharField(primary_key=True, max_length=200)
    password = models.CharField(max_length=200,null=True)
    mobile = models.CharField(max_length=10,null=True)
    email = models.EmailField()
    date_created = models.FloatField()

    def __str__(self):
        return self.username

class LoginStats(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    login_time = models.FloatField(null=True)

    def __str__(self):
        return self.user.username

