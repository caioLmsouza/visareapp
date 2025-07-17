from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Campos extras podem ser adicionados aqui futuramente
    # Exemplo: telefone, tipo de usuário, clínica associada, etc.
    pass 