from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('blogpost/', views.blogpost),
    path('python-intro/', views.python_intro),
    path('django-basics/', views.django_basics),
]
