from django.urls import path,  include
from django.views.generic import RedirectView
from . import views
from .views import *

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('login/', include('contas.urls')),
    path('home/', views.home, name='home'),
    path('evento/cadastro', views.cadastro_evento, name='cadastro_evento'),
    path('evento/<int:pk>', views.evento_detalhe, name='detalhes_evento'),
    path('evento/<int:pk>/editar', views.editar_evento, name='editar_evento'),
    path('evento/', views.listar_evento, name='listar_evento'),
    path('evento/<int:pk>/deletar', views.deletar_evento, name='deletar_evento'),
    path('cadastro_equipe_evento/', EquipeEventoCreateView.as_view(), name='cadastro_equipe_evento'),
    path('deletarcasal/<int:pk>', DeletarCasalView.as_view(), name='deletarcasal'),
    path('casais/', ListaCasaisView.as_view(), name='casais'),
    path('cadastrocasal/', CasalCreateView.as_view(), name='cadastrocasal'),
]
