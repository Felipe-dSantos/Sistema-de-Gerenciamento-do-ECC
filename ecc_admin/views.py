from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventoForm
from .models import Evento
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView, ListView
from django.views import View
from django.http import JsonResponse, HttpResponseRedirect
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
    template_name = 'deletarcasal.html'
    success_url = reverse_lazy('casais')


    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            self.object.delete()
        
            return HttpResponseRedirect(self.get_success_url())
        except Exception as e:
            print("OI")
            return JsonResponse({'success': False, 'error_message': str(e)})


class EquipeEventoCreateView(CreateView):
    model = EquipeEvento
    form_class = EquipeEventoForm
    template_name = 'cadastro_equipe_evento.html'
    success_url = reverse_lazy('listaequipes')

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class ListaEquipesView(ListView):
    model = EquipeEvento
    template_name = 'listaequipes.html'
    context_object_name = 'equipes'


class DeletarEquipeView(DeleteView):
    model = EquipeEvento
    template_name = 'deletarequipe.html'
    success_url = reverse_lazy('listaequipes')


    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            self.object.delete()
        
            return HttpResponseRedirect(self.get_success_url())
        except Exception as e:
            print("OI")
            return JsonResponse({'success': False, 'error_message': str(e)})

class CasalEditView(UpdateView):
    model = Casal
    form_class = CasalEditForm
    template_name = 'editarcasal.html'
    success_url = reverse_lazy('casais')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contatos_casal = Contato.objects.filter(casal=self.object)
        context['contatos'] = [ContatoForm(instance=contato, prefix=f'contato_casal_{contato.id}') for contato in contatos_casal]
        #context['contatos'] = Contato.objects.filter(casal=self.object)
        return context

    def form_valid(self, form):
        # Processa o formulário principal (Casal)
        self.object = form.save()

        # Processa os formulários de Contato
        for key, value in self.request.POST.items():
            if key.startswith('contato_casal_'):
                contato_id = int(key.split('_')[-1].split('-')[0])
                contato = Contato.objects.get(id=contato_id)
                contato_form = ContatoForm(self.request.POST, instance=contato, prefix=contato_id)

                if contato_form.is_valid():
                    print("ooooooooooooooooooooooooooooooooooooooooooooo")
                    contato_form.save()

        return super().form_valid(form)


'''
class CasalEditView(UpdateView):
    model = Casal
    form_class = CasalEditForm
    template_name = 'editarcasal.html'
    success_url = reverse_lazy('casais')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contatos_marido = Contato.objects.filter(casal=self.object, tipo_contato='MARIDO')
        contatos_mulher = Contato.objects.filter(casal=self.object, tipo_contato='MULHER')
        context['contatos_marido'] = [ContatoForm(instance=contato, prefix=f'contato_marido_{contato.id}') for contato in contatos_marido]
        context['contatos_mulher'] = [ContatoForm(instance=contato, prefix=f'contato_mulher_{contato.id}') for contato in contatos_mulher]
        return context

    def form_valid(self, form):
        # Processa o formulário principal (Casal)
        self.object = form.save()

        # Processa os formulários de Contato
        for key, value in self.request.POST.items():
            if key.startswith('contato_marido_') or key.startswith('contato_mulher_'):
                contato_id = int(key.split('_')[-1])
                contato = Contato.objects.get(id=contato_id)
                contato_form = ContatoForm(self.request.POST, instance=contato, prefix=key)
                if contato_form.is_valid():
                    contato_form.save()

        return super().form_valid(form)
'''
