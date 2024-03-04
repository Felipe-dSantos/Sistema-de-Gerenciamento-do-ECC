from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventoForm
from .models import Evento
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import TemplateView, ListView
from django.views import View
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *


@login_required
def home(request):
    return render(request, 'home.html')

def cadastro_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)

        if form.is_valid():
            evento = form.save()
            return redirect('detalhes_evento', pk = evento.pk)
    else: 
        form = EventoForm()
    return render(request, 'cadastro_evento.html', {'form': form})

def evento_detalhe(request, pk):
    evento = get_object_or_404(Evento, pk = pk)
    return render(request, 'detalhes_evento.html', {'evento': evento})

def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk = pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)

        if form.is_valid():
            evento = form.save()
            return redirect('detalhes_evento', pk = evento.pk)
    else: 
        form = EventoForm(instance=evento)
    return render(request, 'editar_evento.html', {'form': form})

def listar_evento(request):
    eventos = Evento.objects.all()
    return render(request, 'lista_eventos.html', {'eventos': eventos})

def deletar_evento(request, pk):
    evento = get_object_or_404(Evento, pk = pk)
    evento.delete()
    return redirect('listar_evento')

def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk = pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)

        if form.is_valid():
            evento = form.save()
            return redirect('detalhes_evento', pk = evento.pk)
    else: 
        form = EventoForm(instance=evento)
    return render(request, 'editar_evento.html', {'form': form})

def listar_evento(request):
    eventos = Evento.objects.all()
    return render(request, 'lista_eventos.html', {'eventos': eventos})

def deletar_evento(request, pk):
    evento = get_object_or_404(Evento, pk = pk)
    evento.delete()
    return redirect('listar_evento')


class CasalCreateView(CreateView):
    model = Casal
    form_class = CasalForm
    template_name = 'cadastrocasal.html'
    success_url = reverse_lazy('casais')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contato_marido_form'] = ContatoForm(prefix='contato_marido')
        context['contato_mulher_form'] = ContatoForm(prefix='contato_mulher')
        return context

    def form_valid(self, form):
        # Salva o objeto principal (Casal)
        self.object = form.save()

        # Processa o formulário ContatoForm para o marido
        contato_marido_form = ContatoForm(self.request.POST, prefix='contato_marido')
        if contato_marido_form.is_valid():
            Contato.objects.create(
                casal=self.object,
                telefone=contato_marido_form.cleaned_data['telefone'],
                email=contato_marido_form.cleaned_data['email']
            )

        # Processa o formulário ContatoForm para a mulher
        contato_mulher_form = ContatoForm(self.request.POST, prefix='contato_mulher')
        if contato_mulher_form.is_valid():
            Contato.objects.create(
                casal=self.object,
                telefone=contato_mulher_form.cleaned_data['telefone'],
                email=contato_mulher_form.cleaned_data['email']
            )

        return super().form_valid(form)


class CadastroCasalSucessoView(TemplateView):
    template_name = 'cadastrocasal_sucesso.html'


class ListaCasaisView(ListView):
    model = Casal
    template_name = 'listacasais.html'
    context_object_name = 'casais'


class DeletarCasalView(DeleteView):
    model = Casal
    template_name = 'void.html'
    success_url = reverse_lazy('casais')


    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            return JsonResponse({'success': True, 'redirect': self.success_url})
#            return super().delete(request, *args, **kwargs)
          #  response = super().delete(request, *args, **kwargs)
          #  return response
        except Exception as e:
            print("OI")
            return JsonResponse({'success': False, 'error_message': str(e)})


class EquipeEventoCreateView(CreateView):
    model = EquipeEvento
    form_class = EquipeEventoForm
    template_name = 'cadastro_equipe_evento.html'
    sucess_url = reverse_lazy('casais')

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)
