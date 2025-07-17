from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.shortcuts import render

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer 

def login_page(request):
    return render(request, 'login.html') 

def dashboard(request):
    return render(request, 'dashboard.html')

def pacientes(request):
    return render(request, 'pacientes.html')

def clinicas(request):
    return render(request, 'clinicas.html')

def consultas(request):
    return render(request, 'consultas.html')

def fichas(request):
    return render(request, 'fichas.html')

def relatorios(request):
    return render(request, 'relatorios.html')

def configuracoes(request):
    return render(request, 'configuracoes.html')

def forgot_password(request):
    return render(request, 'forgot_password.html') 