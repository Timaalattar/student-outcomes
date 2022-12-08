from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Student(models.Model): 
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    linkedin = models.TextField(max_length=250)
    github = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name # Add this method
 
    def get_absolute_url(self):
        return reverse('detail', kwargs={'student_id': self.id})

    

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