from django.utils import timezone
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from uuid import uuid4


class Casal(models.Model):
    STATUS_CASAL_ECC = [
        ('ATIVO', 'Ativo'),
        ('INATIVO', 'Inativo'),
    ]

    STATUS_MATRIMONIO = [
        ('CASADO', 'Casado'),
        ('DIVORCIADO', 'Divorciado'),
    ]

    # informações de marido e mulher
    cpf_marido = models.CharField(max_length=11)
    cpf_mulher = models.CharField(max_length=11)
    primeiro_nome_marido = models.CharField(max_length=40)
    primeiro_nome_mulher = models.CharField(max_length=40)
    sobrenome_marido = models.CharField(max_length=70)
    sobrenome_mulher = models.CharField(max_length=70)
    nascimento_marido = models.DateField()
    nascimento_mulher = models.DateField()

    # informações de casal
    status_casal_ecc = models.CharField(max_length=7, choices=STATUS_CASAL_ECC)
    status_matrimonio = models.CharField(max_length=10, choices=STATUS_MATRIMONIO)
    quantidade_eventos_participados = models.IntegerField()
    data_casamento = models.DateField()

    # endereço
    cep = models.CharField(max_length=9, null=True, blank=True)
    bairro = models.CharField(max_length=70)
    rua = models.CharField(max_length=70)
    numero_residencial = models.CharField(max_length=6)
    referencia = models.CharField(max_length=70, null=True, blank=True)

    # informações adicionais
    data_cadastro = models.DateTimeField(default=timezone.now)
    data_atualizacao = models.DateTimeField(auto_now=True)


class Contato(models.Model):
    telefone = models.CharField(max_length=9, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    casal = models.ForeignKey(Casal, on_delete=models.CASCADE)


class Evento(models.Model):
    num_edicao = models.IntegerField()
    ano_edicao = models.DateField()
    data_registro = models.DateTimeField(default=timezone.now)
    data_atualizacao = models.DateTimeField(default=timezone.now)
class Habilidade(models.Model):
    nome = models.CharField(max_length=60)
    equipe_evento = models.ForeignKey('EquipeEvento', on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)


class EquipeEvento(models.Model):
    nome = models.CharField(max_length=60)
    quantidade_membros = models.IntegerField()
    data_cadastro = models.DateTimeField(default=timezone.now)
    data_atualizacao = models.DateTimeField(auto_now=True)