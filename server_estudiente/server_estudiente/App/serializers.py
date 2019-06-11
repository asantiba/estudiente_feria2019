from rest_framework import serializers
from .models import Dentadura

class DentaduraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentadura
        fields = ('idpaciente', 'iddiente', 'estado', 'Comentario detallado')

    
