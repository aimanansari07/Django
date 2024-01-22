from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bugatti(request):
    return render(request,'bugatti.html')


def lambo(request):
    return render(request,'lamborghini.html')