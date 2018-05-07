from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect

def home(request):
    return HttpResponse("bonjour tout le monde -> vous etes sur la page d'inscription")
