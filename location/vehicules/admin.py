from django.contrib import admin
from .models import Voiture

@admin.register(Voiture)
class VoitureAdmin(admin.ModelAdmin):
    list_display = ['marque', 'nom', 'prix_par_jour', 'prix_final', 'categorie', 'disponible']
    list_filter = ['categorie', 'carburant', 'disponible', 'est_promo']
    search_fields = ['nom', 'marque']
    list_editable = ['prix_par_jour', 'disponible']
    list_per_page = 20
    
    fields = [
        'nom', 'marque', 'prix_par_jour', 'image',
        'categorie', 'carburant', 'nb_places', 'nb_portes', 'annee',
        'description', 'equipements',
        'disponible', 'est_promo', 'reduction_promo'
    ]