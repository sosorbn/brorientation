from django.http import HttpResponse
from django.shortcuts import render,redirect

def inscription(request):
    return render(request,'inscription/sinscrire.html')

def postulant(request):
    return render(request,'inscription/postulant.html')

def intervenant(request):
    return render(request,'inscription/intervenant.html')
