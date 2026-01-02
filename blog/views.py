from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def home_page(request):
    return HttpResponse("Welcome to the Home Page!")

def blogpost(request):
    return HttpResponse("This is a blog post.")

def python_intro(request):
    return HttpResponse("Introduction to Python programming.")

def django_basics(request):
    return HttpResponse("Basics of Django framework.")

def python_oops(request):
    return HttpResponse("Object-Oriented Programming in Python.")

def blog_post(request, blog):
    if blog == "python-intro":
        return python_intro(request)
    elif blog == "django-basics":
        return django_basics(request)
    elif blog == "python-oops":
        return python_oops(request)
    else:
        return HttpResponseNotFound("Blog post not found.")
    return HttpResponse(f"This is the blog post: {blog}")