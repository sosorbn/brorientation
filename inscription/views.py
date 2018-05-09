from django.shortcuts import render
from .forms import *
from inscription.models import *
from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    return HttpResponse("bonjour tout le monde -> vous étes sur une page d'inscription")

def get_intervenant_infos(request):

    form = intervenantForm(request.POST or None)
    if form.is_valid():
        nom = form.cleaned_data['intervenant_nom']
        prenom = form.cleaned_data['intervenant_prenom']
        password = form.cleaned_data['intervenant_password']
        passwordConfirmation = form.cleaned_data['intervenant_passwordConfirmation']
        date= form.cleaned_data['date_naissance']
        adresse = form.cleaned_data['adresse_mail']
        inscription = True
        return HttpResponse(nom)


    return render(request,'inscription/formulaire.html',locals())
