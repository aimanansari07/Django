from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def samsung(request):
    return HttpResponse("samsung z fold")

def google(request):
    return HttpResponse("google pixel")
