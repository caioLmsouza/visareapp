from django.db import models

# Create your models here.

class Clinica(models.Model):
    nome = models.CharField("Nome da clínica", max_length=255)
    cnpj = models.CharField("CNPJ", max_length=18, unique=True)
    # Endereço detalhado
    rua = models.CharField("Rua", max_length=255, blank=True, null=True)
    numero = models.CharField("Número", max_length=10, blank=True, null=True)
    bairro = models.CharField("Bairro", max_length=100, blank=True, null=True)
    cidade = models.CharField("Cidade", max_length=100, blank=True, null=True)
    uf = models.CharField("UF", max_length=2, blank=True, null=True)
    cep = models.CharField("CEP", max_length=10, blank=True, null=True)
    # Contato
    telefone = models.CharField("Telefone", max_length=20, blank=True, null=True)
    email = models.EmailField("E-mail", blank=True, null=True)
    site = models.URLField("Site", blank=True, null=True)
    responsavel = models.CharField("Responsável", max_length=255)
    # Personalização
    logo = models.ImageField("Logo", upload_to='logos/', blank=True, null=True)
    tema_visual = models.CharField("Tema visual", max_length=50, blank=True, null=True)
    # Documentos
    cabecalho_documento = models.TextField("Cabeçalho de documento", blank=True, null=True)
    rodape_documento = models.TextField("Rodapé de documento", blank=True, null=True)
    observacoes = models.TextField("Observações", blank=True, null=True)
    data_cadastro = models.DateTimeField("Data de cadastro", auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
