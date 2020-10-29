from django.db import models

# Create your models here.
class Register(models.Model):
    userid = models.AutoField(primary_key=True,default=1)
    name = models.CharField(max_length=200,null=True)
    username = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200,null=True)
    mobile = models.CharField(max_length=10,null=True)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
