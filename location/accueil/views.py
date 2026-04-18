from django.shortcuts import render
from vehicules.models import Voiture

def accueil(request):
    # Get all available cars from database
    cars = Voiture.objects.filter(disponible=True)

    return render(request, 'accueil.html', {'cars': cars})