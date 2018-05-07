from django.http import HttpResponse
from django.shortcuts import render,redirect

def userspace(request):
    return render(request,"userSpace/userSpace.html")

def rechercher(request):
    return render(request,"userSpace/rechercher.html")

def historique(request):
    return render(request,"userSpace/historique.html")

def messagerie(request):
    return render(request,"userSpace/messagerie.html")

def mesinfos(request):
    return render(request,"userSpace/mesinfos.html")
