import string
from urllib import request, response
from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalBackend import serializers
from hospitalBackend.serializers.medicoSerializer import MedicoSerializer
from hospitalBackend.serializers.usuarioSerializer import UsuarioSerializer
from hospitalBackend.models.medico import Medico

class MedicoListCreateView(generics.ListCreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los Medico")
        queryset = self.get_queryset()  #ES EL MISMO QUERYSET DE AFUERA, BASICAMENTE ES DECIRLE QUE TRAIGA TODOS LOS USER
        serializer = MedicoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("POST a Medico")
        print(request.data)  #VERIFICA LA INFORMACIÓN QUE MANDÓ EL USUARIO DESDE FE, O SEA EL JSON DEBE ESTAR AHÍ, CUANDO EL JSON LO OBTIENE EL FRAMEWORK LO PASA A DICCIONARIO
        
        
        usuarioData = request.data.pop('usuario') #El request.data es como se accede a la info, el pop repera la info del diccionario y lo saca y lo pone en la variable
        serializerU = UsuarioSerializer(data = usuarioData)
        serializerU.is_valid(raise_exception=True) #Verifica si la información es valida
        usuario = serializerU.save()


        enfData = request.data
        enfData.update({"usuario":usuario.id})

        serializerEnf = MedicoSerializer(data = enfData)
        serializerEnf.is_valid(raise_exception=True)
        serializerEnf.save()
        return Response(status=status.HTTP_201_CREATED)

        #tokenData = {
        #    "username":request.data["username"],
        #    "password":request.data["password"]
        #    }
        #tokenSerializer= TokenObtainPairSerializer(data=tokenData)
        #tokenSerializer.is_valid(raise_exception=True)
        #Return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

class MedicoRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset= Medico.objects.all()
    serializer_class= MedicoSerializer
    lookup_field= "id"   #campo de busqueda de objetos
    lookup_url_kwarg= 'pk'   #Es lo que va en la URL


    def get(self,request, *args, **kwargs):
        print("GET a Medico")
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a Medico")
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().put(request, *args, **kwargs)

    
    def delete(self, request, *args, **kwargs):
        print("DELETE a Medico")
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().delete(request, *args, **kwargs)   #AL PONER SUPER, SE VA A LA CLASE SUPERIOR
