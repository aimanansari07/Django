from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hayabusa(request):
    return render(request,'hayabusa.html')


def ninja(request):
    return render(request,'ninja.html')