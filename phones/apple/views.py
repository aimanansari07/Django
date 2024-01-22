from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def iphone(request):
    return HttpResponse("iphone 11 ")

def mac(request):
    return HttpResponse("macbook pro")

