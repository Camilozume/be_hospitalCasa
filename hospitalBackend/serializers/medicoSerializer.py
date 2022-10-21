from dataclasses import fields
from string import printable
from rest_framework import serializers
from hospitalBackend.models.medico import Medico


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:  #Guia para que el framework sepa cómo moverse
        model =Medico
        fields= ['id', 'especialidad', 'registro', 'usuario']