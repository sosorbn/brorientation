from django import forms
from .models import *

class PostulantForm(forms.Form):
    postulant_nom = forms.CharField(label='Nom',max_length=100, required=True)
    postulant_prenom = forms.CharField(label='Prénom',max_length=100, required=True)
    postulant_description = forms.CharField(label = 'Description Personelle', max_length=500)
    postulant_mail = forms.EmailField(label="Votre adesse e-mail", required=True)
    postulant_date_naissance = forms.DateTimeField(label="Date de naissance", required = True)
    postulant_photo = forms.ImageField()
    postulant_mdp = forms.CharField(max_length=32, widget=forms.PasswordInput)
    postulant_confirmation = forms.CharField(max_length=32, widget=forms.PasswordInput)

class intervenantForm(forms.Form):
    intervenant_prenom = forms.CharField(
        label = "Prenom:",
        required = True,
        widget = forms.TextInput(attrs={
            'class': 'form-control', 'placeholder' : 'Prénom'
        }))
    intervenant_nom = forms.CharField(
        label = "Nom:",
        required = True,
        widget = forms.TextInput(attrs={
            'class': 'form-control' , 'placeholder' : 'Nom'
        }))
    date_naissance = forms.DateField(
        label = "date de naissance:",
        required = True,
        widget = forms.DateInput(attrs={
            'class': 'form-control', 'placeholder' : 'JJ/MM/AAAA'
        }))
    adresse_mail = forms.EmailField(
        label= "adresse mail:",
        required = True,
        widget = forms.EmailInput(attrs={
            'class': 'form-control', 'placeholder' : 'exemple : jojo@gmail.com'
        }))
    intervenant_password = forms.CharField(
        label="password:",
        required = True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control' ,'placeholder' : 'password'
        }))
    intervenant_passwordConfirmation = forms.CharField(
        label = "password confirmation:" ,
        required = True,
        widget = forms.PasswordInput(attrs={
            'class': 'form-control', 'placeholder' : 'passwordConfirmation'
        }))
