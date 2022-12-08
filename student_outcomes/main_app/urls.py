from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:student_id>/', views.detail, name='detail'),
    path('student/create/', views.StudentCreate.as_view(), name='student_create'),
    path('detail/<int:pk>/update/', views.StudentUpdate.as_view(), name='detail_update'),
    path('detail/<int:pk>/delete/', views.StudentDelete.as_view(), name='detail_delete'),
    path('profile/', views.profile, name='profile'),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('profile/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profile_delete'),
    path('projects/', views.projects, name='projects'),
    path('projects/create/', views.ProjectCreate.as_view(), name='student_create'),
    path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='projects_update'),
    path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='projects_delete'),
    path('index/', views.index, name='index'),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
    path('project/create/', views.ProjectCreate.as_view(), name='project_create'),
    path('accounts/signup', views.signup, name='signup'),
]