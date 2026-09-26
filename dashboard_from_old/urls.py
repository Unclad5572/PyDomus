from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('historique/', views.historique, name='historique'),
    path('alertes/', views.alertes, name='alertes'),
]