from django import forms
from .models import Evento
from .models import *
from django.forms import DateInput
from django.utils import timezone

class EventoForm (forms.ModelForm):
    class Meta: 
        model = Evento
        fields = '__all__'
        

class CasalForm(forms.ModelForm):
    class Meta:
        model = Casal

        fields = ['primeiro_nome_marido', 'sobrenome_marido', 
                  'cpf_marido', 'nascimento_marido', 
                  'primeiro_nome_mulher', 'sobrenome_mulher', 
                  'cpf_mulher', 'nascimento_mulher', 
                  'cep', 'bairro', 'rua', 'numero_residencial', 
                  'referencia', 'status_casal_ecc', 
                  'status_matrimonio', 'data_casamento']

        widgets = {
            'nascimento_marido': DateInput(attrs={'type': 'date'}),
            'nascimento_mulher': DateInput(attrs={'type': 'date'}),
            'data_casamento': DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        casal = super().save(commit=False)

        # Informações preenchidas automaticamente
        casal.quantidade_eventos_participados = 0
        casal.data_cadastro = timezone.now()
        casal.data_atualizacao = timezone.now()

        if commit:
            casal.save()
        return casal


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['telefone', 'email']

    def save(self, casal, commit=True):
        contato = super().save(commit=False)
        contato.casal = casal
        if commit:
            contato.save()
        return contato


class EquipeEventoForm(forms.ModelForm):
    class Meta:
        model = EquipeEvento
        fields = ['nome', 'quantidade_membros']


    def save(self, commit=True):
        equipe_evento = super().save(commit=False)
        equipe_evento.data_cadastro = timezone.now()
        equipe_evento.data_atualizacao = timezone.now()

        if commit:
            equipe_evento.save()
        return equipe_evento


class HabilidadeForm(forms.ModelForm):
    class Meta:
        model = Habilidade
        fields = ['nome']

    
    def save(self, commit=True):
        habilidade = super().save(commit=False)
        habilidade.data_cadastro = timezone.now()
        habilidade.data_atualizacao = timezone.now()


        if commit:
            habilidade.save()
        return habilidade

class CasalEditForm(forms.ModelForm):
    class Meta:
        model = Casal
        fields = '__all__'


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'

