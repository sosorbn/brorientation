from django.urls import path
from . import views

urlpatterns = [
    path('',views.userspace),
    path('rechercher',views.rechercher),
    path('historique',views.historique),
    path('messagerie',views.messagerie),
    path('mesinfos',views.mesinfos),
]
