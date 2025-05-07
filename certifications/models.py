
from django.db import models
from utilisateurs.models import Utilisateur

class Certification(models.Model):
    competence = models.CharField(max_length=255)
    apprenant = models.ForeignKey(Utilisateur, related_name='certifications', on_delete=models.CASCADE)
    mentor = models.ForeignKey(Utilisateur, related_name='validations', on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    hash_blockchain = models.CharField(max_length=255, blank=True, null=True)
# Create your models here.
