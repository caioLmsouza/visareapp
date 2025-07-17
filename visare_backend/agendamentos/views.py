from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Agendamento
from .serializers import AgendamentoSerializer

# Create your views here.

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
