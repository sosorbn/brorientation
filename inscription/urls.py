from django.urls import path
from . import views

urlpatterns = [
    path('sinscrire',views.inscription),
    path('postulant',views.postulant),
    path('intervenant',views.intervenant)

]
