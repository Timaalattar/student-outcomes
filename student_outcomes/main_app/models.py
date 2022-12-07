from django.db import models

# Create your models here.

class Student(models.Model): 
    email = models.CharField(max_length=100)
    Mobile = models.IntegerField(max_length=8)
    Linkedin = models.TextField(max_length=250)
    Github = models.TextField(max_length=250)

class Profile(models.Model): 
    education = models.CharField(max_length=500)
    work = models.CharField(max_length=1000)
    skills = models.CharField(max_length=1000)

class Project(models.Model): 
    Title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=1000)
    technology = models.CharField(max_length=1000)