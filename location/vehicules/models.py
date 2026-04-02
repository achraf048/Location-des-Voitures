from django.db import models

class Voiture(models.Model):
    nom = models.CharField(max_length=100)
    marque = models.CharField(max_length=50)
    prix_par_jour = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=200, blank=True, null=True)
    
    # Optional fields - can be NULL if not provided
    categorie = models.CharField(max_length=50, blank=True, null=True)  
    carburant = models.CharField(max_length=50, blank=True, null=True)   
    nb_places = models.IntegerField(null=True, blank=True)
    nb_portes = models.IntegerField(null=True, blank=True)
    annee = models.IntegerField(null=True, blank=True)
    
    description = models.TextField(blank=True, null=True)
    equipements = models.TextField(blank=True, null=True, help_text="GPS, Climatisation, etc.")
    
    disponible = models.BooleanField(default=True)
    est_promo = models.BooleanField(default=False)
    reduction_promo = models.IntegerField(null=True, blank=True, help_text="Pourcentage de réduction (0-100)")
    
    # Meta
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.marque} {self.nom}"
    
    @property
    def prix_final(self):
        """Returns price after discount if promo is active"""
        if self.est_promo and self.reduction_promo:
            return self.prix_par_jour * (1 - self.reduction_promo / 100)
        return self.prix_par_jour
    
    class Meta:
        ordering = ['-date_ajout']