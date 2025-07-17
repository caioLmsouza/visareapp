from django.db import models
from pacientes.models import Paciente
from clinicas.models import Clinica

class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='agendamentos')
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE, related_name='agendamentos')
    data_hora = models.DateTimeField()
    profissional = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    observacoes = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Agendamento em {self.data_hora} (ID: {self.pk})'
