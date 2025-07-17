from django.db import models

# Create your models here.

class Paciente(models.Model):
    nome = models.CharField("Nome completo", max_length=255)
    cpf = models.CharField("CPF", max_length=14, unique=True)
    rg = models.CharField("RG", max_length=20, blank=True, null=True)
    data_nascimento = models.DateField("Data de nascimento", blank=True, null=True)
    genero = models.CharField("Gênero", max_length=20, blank=True, null=True, choices=[('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outro')])
    email = models.EmailField("E-mail", blank=True, null=True)
    telefone = models.CharField("Telefone", max_length=20, blank=True, null=True)
    responsavel = models.CharField("Responsável", max_length=255, blank=True, null=True)
    convenio = models.CharField("Convênio/Plano de Saúde", max_length=100, blank=True, null=True)
    # Endereço
    rua = models.CharField("Rua", max_length=255, blank=True, null=True)
    numero = models.CharField("Número", max_length=10, blank=True, null=True)
    bairro = models.CharField("Bairro", max_length=100, blank=True, null=True)
    cidade = models.CharField("Cidade", max_length=100, blank=True, null=True)
    uf = models.CharField("UF", max_length=2, blank=True, null=True)
    cep = models.CharField("CEP", max_length=10, blank=True, null=True)
    observacoes = models.TextField("Observações", blank=True, null=True)
    historico_medico = models.TextField("Histórico médico", blank=True, null=True)
    anamnese = models.TextField("Anamnese", blank=True, null=True)
    data_cadastro = models.DateTimeField("Data de cadastro", auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
