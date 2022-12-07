from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/', views.student, name='student'),
    path('profile/', views.profile, name='profile'),
    path('projects/', views.projects, name='projects'),
    path('index/', views.index, name='index'),
]