from rest_framework import serializers
from hospitalBackend.models.usuario import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:  #Guia para que el framework sepa cómo moverse
        model = Usuario
        fields= ['id', 'rol', 'username', 'password', 'apellido', 'e_mail', 'celular', 'direccion']