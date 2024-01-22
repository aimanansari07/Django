from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hayabusa(request):
    return HttpResponse("hayabusa")

def ninja(request):
    return HttpResponse("ninja h2r")