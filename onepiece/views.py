from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ennies_lobby(request):
    return HttpResponse('<h1>LUFFY DECLARED WAR ON WORLD GOVERNEMENT IN ENNIES LOBBY TO SAVE ROBIN</h1>')

def wano(request):
    return HttpResponse('<h1>IN WANO WE GET TO KNOW THAT LUFFY IS SUN GOD NIKA</h1>')
