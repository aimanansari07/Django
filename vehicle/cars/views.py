from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bugatti(request):
    return HttpResponse("bugatti")

def lambo(request):
    return HttpResponse("lamborghini")