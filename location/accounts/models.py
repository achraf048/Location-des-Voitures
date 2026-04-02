from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    # Optional contact info
    telephone = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    permis_valide = models.BooleanField(default=False)
    date_naissance = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.username