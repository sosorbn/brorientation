from django.urls import path
from . import views

urlpatterns = [
    path('accueilVisiteur',views.home),
    path('help',views.help)
]
