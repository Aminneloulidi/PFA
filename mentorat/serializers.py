from rest_framework import serializers
from .models import DemandeMentorat  # Assurez-vous que ce modèle existe

class DemandeMentoratSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeMentorat
        fields = '__all__'  # Inclure tous les champs du modèle