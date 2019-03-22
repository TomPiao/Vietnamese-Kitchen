from django.urls import path
from . import views

url_patterns = [
    path('home/', views.HomeView.as_view(), name='home')
]
