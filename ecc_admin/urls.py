from django.urls import path,  include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('login/', include('contas.urls')),
    path('home/', views.home, name='home'),
    path('evento/cadastro', views.cadastro_evento, name='cadastro_evento'),
    path('evento/<int:pk>', views.evento_detalhe, name='detalhes_evento'),
    path('evento/<int:pk>/editar', views.editar_evento, name='editar_evento'),
]
