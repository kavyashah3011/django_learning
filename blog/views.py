from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Welcome to the Home Page!")

def blogpost(request):
    return HttpResponse("This is a blog post.")

def python_intro(request):
    return HttpResponse("Introduction to Python programming.")

def django_basics(request):
    return HttpResponse("Basics of Django framework.")

