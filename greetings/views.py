from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greet(request):
    return HttpResponse("Hello World")

def greet_to_u(request, a):
    a = str(a).capitalize()
    return HttpResponse(f"Hello {a}")