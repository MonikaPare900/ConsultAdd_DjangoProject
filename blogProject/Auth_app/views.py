from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def print_hello(request):
    return HttpResponse("Hello World")
