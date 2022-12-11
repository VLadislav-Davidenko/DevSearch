from django.urls import path
from . import views

# python3 manage.py runserver

urlpatterns = [
    path('', views.getRoutes),
    path('projects/', views.getProjects),
    path('projects/<str:pk>/', views.getProject),
]

