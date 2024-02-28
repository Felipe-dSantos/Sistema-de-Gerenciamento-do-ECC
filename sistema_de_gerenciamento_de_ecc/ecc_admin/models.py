from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from uuid import uuid4




class Endereco(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
     
    ESTADOS_BRASILEIROS = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )

    estado = models.CharField(max_length=20, choices=ESTADOS_BRASILEIROS)
    cidade = models.CharField(max_length=40, validators=[MinLengthValidator(3)])
    bairro = models.CharField(max_length=60, validators=[MinLengthValidator(3)])
    rua = models.CharField(max_length=70, validators=[MinLengthValidator(2)])
    cep = models.CharField(max_length=9, validators=[MinLengthValidator(8)])
    numero_residencial = models.CharField(max_length=6, validators=[MinLengthValidator(1)])
    referencia = models.CharField(max_length=30)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)


class Contato(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    telefone = models.CharField(max_length=11, null=True)
    email = models.EmailField(max_length=100, null=True)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)



class MembroIgreja(models.Model):
    SEXO = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )

    cpf = models.CharField(max_length=11, unique=True)
    primeiro_nome = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    segundo_nome = models.CharField(max_length=40, validators=[MinLengthValidator(2)])
    nascimento = models.DateTimeField()
    sexo = models.CharField(max_length=1, choices=SEXO)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    contato = models.ForeignKey(Contato, on_delete=models.SET_NULL, null=True)
    data_registro = models.DateTimeField(auto_now=True)
    data_atualizacao = models.DateTimeField(auto_now=True)



class Casal(models.Model):
    STATUS_CASAL_ECC = (
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    )
    STATUS_MATRIMONIO = (
        ('casado', 'Casado'),
        ('divorciado', 'Divorciado'),
    )

    cpf_marido = models.ForeignKey(MembroIgreja, on_delete=models.CASCADE, related_name='marido')
    cpf_esposa = models.ForeignKey(MembroIgreja, on_delete=models.CASCADE, related_name='esposa')
    id = models.CharField(max_length=22, primary_key=True)  # 11 para cpf_marido and 11 para cpf_esposa
    data_casamento = models.DateTimeField()
    status_casal_ecc = models.CharField(max_length=7, choices=STATUS_CASAL_ECC)
    status_matrimonio = models.CharField(max_length=10, choices=STATUS_MATRIMONIO)
    data_cadastro_casal = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    quantidade_eventos_participados = models.IntegerField()


class EquipeDirigente(models.Model):
    STATUS_CHOICES = (
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    )

    cpf_marido = models.ForeignKey(MembroIgreja, on_delete=models.CASCADE, related_name='marido_dirigente')
    cpf_esposa = models.ForeignKey(MembroIgreja, on_delete=models.CASCADE, related_name='esposa_dirigente')
    id = models.CharField(max_length=22, primary_key=True)  # 11 para cpf_marido e 11 para cpf_esposa
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)
    senha = models.CharField(max_length=512, null=False)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)


class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False)
    equipe_criadora = models.ForeignKey(EquipeDirigente, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)



class EquipeEvento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=60, null=False)
    equipe_criadora = models.ForeignKey(EquipeDirigente, on_delete=models.CASCADE)
    quantidade_membros = models.IntegerField(null=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)



class EdicaoEvento(models.Model):
    id = models.DateTimeField(auto_now_add=True, primary_key=True)
    nome = models.CharField(max_length=60, null=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    equipe_dirigente = models.ForeignKey(EquipeDirigente, on_delete=models.CASCADE)



class ConviteEvento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    casal = models.ForeignKey('Casal', on_delete=models.CASCADE)
    equipe_evento = models.ForeignKey('EquipeEvento', on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aceito', 'Aceito'),
        ('recusado', 'Recusado'),
    ]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    justificativa = models.CharField(max_length=100, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)



class Habilidade(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    equipe_evento = models.ForeignKey('EquipeEvento', on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)



class CasalHabilidade(models.Model):
    id = models.AutoField(primary_key=True)
    casal = models.ForeignKey('Casal', on_delete=models.CASCADE)
    habilidade = models.ForeignKey('Habilidade', on_delete=models.CASCADE)


class CasalEdicaoEvento(models.Model):
    id = models.AutoField(primary_key=True)
    casal = models.ForeignKey('Casal', on_delete=models.CASCADE)
    edicao_evento = models.ForeignKey('EdicaoEvento', on_delete=models.CASCADE)
    equipe_evento = models.ForeignKey('EquipeEvento', on_delete=models.CASCADE)

