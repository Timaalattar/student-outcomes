from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:student_id>/', views.detail, name='detail'),
    path('profile/', views.profile, name='profile'),
    path('projects/', views.projects, name='projects'),
    path('index/', views.index, name='index'),
    path('student/create/', views.StudentCreate.as_view(), name='student_create'),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
    path('project/create/', views.ProjectCreate.as_view(), name='project_create'),
    path('accounts/signup', views.signup, name='signup'),
]