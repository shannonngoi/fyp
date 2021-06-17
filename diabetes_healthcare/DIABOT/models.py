from django.db import models
'''from django.utils import timezone '''
from django.contrib.auth.models import User

# Create your models here.


class ToDo(models.Model):
    task = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

'''

class Post(models.Model):
    tilte = models.CharField(max_length=30)
    content = models.TextField()
    date_login = models.DatetimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    '''

#patient
class addUser(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    gender  = models.CharField(max_length=15)
    martial = models.CharField(max_length=15)