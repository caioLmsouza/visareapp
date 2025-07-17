from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Receita
from .serializers import ReceitaSerializer

# Create your views here.

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    permission_classes = [permissions.IsAuthenticated]
