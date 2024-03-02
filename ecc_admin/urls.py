from django.urls import path,  include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('login/', include('contas.urls')),
    path('home/', views.home, name='home'),
]
