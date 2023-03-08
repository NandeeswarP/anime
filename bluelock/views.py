from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def soccer(request):
    return HttpResponse("<h1>ISAGI IS THE PROTAGANIST IN BLUE LOCK</h1>")

def ego(request):
    return HttpResponse("<h1>EGO IS THE ONE WHO IS RUNNING BLUELOCK</h1>")