from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Endereco)
admin.site.register(Contato) 
admin.site.register(MembroIgreja)
admin.site.register(Casal)
admin.site.register(EquipeDirigente)
admin.site.register(Evento)
admin.site.register(EquipeEvento)
admin.site.register(EdicaoEvento)
admin.site.register(ConviteEvento)
admin.site.register(Habilidade)
admin.site.register(CasalHabilidade)
admin.site.register(CasalEdicaoEvento )


