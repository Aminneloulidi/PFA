from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(AbstractUser):
    ROLES = (
        ('apprenant', 'Apprenant'),
        ('mentor', 'Mentor'),
        ('admin', 'Administrateur'),
    )
    role = models.CharField(max_length=20, choices=ROLES)
    domaines_expertise = models.TextField(blank=True, null=True)  # Pour mentors
# Create your models here.
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Nom unique
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Nom unique
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )