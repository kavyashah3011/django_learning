from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

def blogpost(request):
    return HttpResponse("Hello from Blog")

def home(request):
    res_data = render_to_string('blogs/index.html')
    return HttpResponse(res_data)