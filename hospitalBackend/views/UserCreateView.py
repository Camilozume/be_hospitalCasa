from os import stat
from urllib import request, response
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalBackend.serializers.usuarioSerializer import UsuarioSerializer

class UserCreateView(views.APIView):
    def post(self, request, **kwargs):
        serializer = UsuarioSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData={
            "username":request.data["username"],
            "password":request.data["password"],
        }

        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validate_data, status=status.HTTP_201_CREATED)
        