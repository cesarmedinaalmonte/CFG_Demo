from .models import Escuela, Profesor
from rest_framework import serializers


class EscuelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escuela
        fields = ('nombre', 'direccion', 'telefono', 'publica')


class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('id', 'nombre', 'apellidos', 'escuela')
