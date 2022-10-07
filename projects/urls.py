from django.urls import path
from . import views

# python3 manage.py runserver

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name="single-project"),
    path('create-project', views.createProject, name="create-project"),
    path('update-project/<str:pk>/', views.updateProject, name="update-project"), 
    path('delete-project/<str:pk>/', views.deleteProject, name="delete-project"), 

]

