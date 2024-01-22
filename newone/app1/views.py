from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def marval(request):
    return HttpResponse("Spider-man")

def dc(request):
    return HttpResponse("Bat-man")