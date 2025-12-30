from django.shortcuts import render
from django.http import HttpResponse

def blogpost(request):
    return HttpResponse("Hello from Blog")
