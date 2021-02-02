from django.db import models

# Create your models here.

class User(models.Model):#登陆表
    STType=(
        ('Student','学生'),
        ('Teacher','导师')
    )
    Account = models.CharField(max_length=20,unique=True)
    Password = models.CharField(max_length=30)
    Type = models.CharField(max_length=30,choices=STType,default='学生')

    def __str__(self):
        return  self.Account
