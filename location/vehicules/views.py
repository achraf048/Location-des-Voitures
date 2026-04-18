from django.shortcuts import render, get_object_or_404
from .models import Voiture


def voiture_detail(request, id):
    car = get_object_or_404(Voiture, id=id)
    return render(request, 'voiture_detail.html', {'car': car})