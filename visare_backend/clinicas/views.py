from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Clinica
from .serializers import ClinicaSerializer

# Create your views here.

class ClinicaViewSet(viewsets.ModelViewSet):
    queryset = Clinica.objects.all()
    serializer_class = ClinicaSerializer
    permission_classes = [permissions.IsAuthenticated]
