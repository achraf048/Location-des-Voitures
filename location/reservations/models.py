from django.db import models
from accounts.models import Utilisateur
from vehicules.models import Voiture

class Reservation(models.Model):
    # Status as free text, no restrictions
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('confirmee', 'Confirmée'),
        ('annulee', 'Annulée'),
        ('terminee', 'Terminée'),
    ]
    
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='reservations')
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE, related_name='reservations')
    
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    montant_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_reservation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.utilisateur.username} - {self.voiture}"
    
    def calculer_montant(self):
        """Calculate total price based on days and car price"""
        jours = (self.date_fin - self.date_debut).days
        if jours <= 0:
            jours = 1
        return jours * self.voiture.prix_final