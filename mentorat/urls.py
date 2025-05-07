from django.urls import path
from . import views  # Importez vos vues ici

# Définissez les URL de l'application mentorat
urlpatterns = [
    # Exemple : URL pour gérer les demandes de mentorat
    path('demandes/', views.DemandeMentoratView.as_view(), name='demandes'),
]