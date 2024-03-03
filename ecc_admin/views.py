from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventoForm
@login_required
def home(request):
    return render(request, 'home.html')

def cadastro_evento(request):
    if request.method == 'post':
        form = EventoForm(request.post)

        if form.is_valid():
            evento = form.save()
            # return redirect('evento_detalhe', pk = evento.pk)
    else: 
        form = EventoForm()
    return render(request, 'cadastro_evento.html', {'form': form})