from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventoForm
from .models import Evento
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
