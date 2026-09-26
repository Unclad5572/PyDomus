from django.shortcuts import render

def accueil(request):
    return render(request, 'dashboard/accueil.html')

def historique(request):
    return render(request, 'dashboard/historique.html')

def alertes(request):
    return render(request, 'dashboard/alertes.html')