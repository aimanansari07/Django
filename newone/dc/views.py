from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def superman(request):
    return HttpResponse('i am superman')

def batman(request):
    return HttpResponse('i am batman')