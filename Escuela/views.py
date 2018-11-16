from django.shortcuts import render
from rest_framework import viewsets

from Escuela.models import Escuela, Profesor
from .serializers import EscuelaSerializer, ProfesorSerializer


# Create your views here.
class EscuelaView(viewsets.ModelViewSet):
    # authentication_class = (JSONWebTokenAuthentication,)
    # permission_classes =
    #permission_classes = ()
    queryset = Escuela.objects.all()
    serializer_class = EscuelaSerializer

class ProfesorView(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
