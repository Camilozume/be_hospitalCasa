from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from hospitalBackend.models.paciente import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Paciente
        fields = ('usuario', 'medico')
