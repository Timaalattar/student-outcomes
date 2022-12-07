from django.shortcuts import render, redirect
# import django http 
from django.http import HttpResponse
# we also have to import everything in django including the class functions 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student
from .models import Profile
from .models import Project

# Define the home view
def home(request):
  return HttpResponse('homepage')

def profile(request):
  return render(request, 'profile.html')

def projects(request):
  return render(request, 'projects.html')


def student(request, student_id):
  student = Student.objects.get(id=student_id)
  # instantiate FeedingForm to be rendered in the template
  return render(request, 'student.html')

# Create your views htere.
