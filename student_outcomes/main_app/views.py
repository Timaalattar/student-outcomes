from django.shortcuts import render, redirect
# import django http 
from django.http import HttpResponse
# we also have to import everything in django including the class functions 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student
from .models import Profile
from .models import Project
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Define the home view

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
  return render(request, 'home.html')

def profile(request):
  return render(request, 'profile.html')

def projects(request):
  return render(request, 'projects.html')

def index(request):
  students = Student.objects.all()
  return render(request, 'index.html', { 'students': student })


def student(request, student_id):
  student = Student.objects.get(id=student_id)
  # instantiate FeedingForm to be rendered in the template
  return render(request, 'student/detail.html', { 'students': student })

# Create your views htere.
