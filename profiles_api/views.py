
from email import message
from http.client import responses
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sympy import re

from profiles_api import serializers


# Create your views here.

class HelloApiView(APIView):
    """api View de prueba"""

    serializer_class = serializers.HelloSerializers

    def get(self,request,format=None):
        """retornar lista de caracteristicas  del Apiview"""
        an_apview = [
            'Usamos metodos HTTP como funciones (get, post,patch,put,delete)',
            'Es similar a una vista tradicional de django'
            'Nos da mayor control de la logica de la aplicacion'
            'Esta mapeado manualmente los  URLs'
        ]

        return Response({'message':'hello', 'an_apiview' : an_apview})

    def post(self,request):
        """Crea un mensaje con nuestro nombre"""
        serializer =  self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello{name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Maneja  actualizar un objeto"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """maneja actulizacion de objetos"""
        return Response({'method':'PATCH'})

    
    def delete(self,request,pk=None):
        """Elimina objetos"""
        return Response({'method':'DELETE'})
            

