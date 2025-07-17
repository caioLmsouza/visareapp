from django.db import models
from pacientes.models import Paciente
from clinicas.models import Clinica
from agendamentos.models import Agendamento

class Receita(models.Model):
    STATUS_CHOICES = [
        ('rascunho', 'Rascunho'),
        ('emitida', 'Emitida'),
        ('cancelada', 'Cancelada'),
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='receitas')
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE, related_name='receitas')
    agendamento = models.ForeignKey(Agendamento, on_delete=models.SET_NULL, blank=True, null=True, related_name='receitas')
    data_emissao = models.DateTimeField(auto_now_add=True)
    prescricao_oculos = models.TextField(blank=True, null=True)
    prescricao_lentes = models.TextField(blank=True, null=True)
    anamnese = models.TextField(blank=True, null=True)
    atestados = models.TextField(blank=True, null=True)
    documentos = models.TextField(blank=True, null=True)
    anexos = models.TextField(blank=True, null=True)  # Pode ser FileField futuramente
    personalizacao = models.JSONField(blank=True, null=True)  # Para cabeçalho, rodapé, logo, etc.
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='rascunho')
    data_criacao = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Receita {self.pk} em {self.data_emissao}'
