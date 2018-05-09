from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('formulaireIntervenant',views.get_intervenant_infos, name = 'get_intervenant_infos')
]
