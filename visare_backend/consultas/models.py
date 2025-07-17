from django.db import models
from pacientes.models import Paciente
from core.models import CustomUser
from clinicas.models import Clinica

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    profissional = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='consultas')
    clinica = models.ForeignKey(Clinica, on_delete=models.SET_NULL, null=True, related_name='consultas')
    data_hora_inicio = models.DateTimeField()
    data_hora_fim = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('Agendada','Agendada'),('Realizada','Realizada'),('Cancelada','Cancelada'),('Vencida','Vencida'),('Em atendimento','Em atendimento')], default='Agendada')
    urgencia = models.CharField(max_length=10, choices=[('Baixa','Baixa'),('Média','Média'),('Alta','Alta')], default='Baixa')
    tipo = models.CharField(max_length=30, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.paciente} - {self.data_hora_inicio:%d/%m/%Y %H:%M}" 