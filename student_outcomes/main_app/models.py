from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model): 
    email = models.CharField(max_length=100)
    Mobile = models.IntegerField(max_length=8)
    Linkedin = models.TextField(max_length=250)
    Github = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Profile(models.Model): 
    education = models.CharField(max_length=500)
    work = models.CharField(max_length=1000)
    skills = models.CharField(max_length=1000)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Project(models.Model): 
    Title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=1000)
    technology = models.CharField(max_length=1000)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)