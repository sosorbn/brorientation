from django.http import HttpResponse
from django.shortcuts import render,redirect

def home(request):
    return HttpResponse("bonjour tout le monde -> vous êtes sur la page userSpace")
