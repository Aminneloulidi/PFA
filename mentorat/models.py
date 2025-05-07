from django.db import models
from utilisateurs.models import Utilisateur

class DemandeMentorat(models.Model):
    apprenant = models.ForeignKey(Utilisateur, related_name='demandes', on_delete=models.CASCADE)
    mentor = models.ForeignKey(Utilisateur, related_name='demandes_recues', on_delete=models.CASCADE)
    competence = models.CharField(max_length=255)
    statut = models.CharField(max_length=20, choices=[('en_attente', 'En Attente'), ('acceptee', 'Acceptée'), ('refusee', 'Refusée')], default='en_attente')
    date_demande = models.DateTimeField(auto_now_add=True)
# Create your models here.
