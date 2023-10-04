from django.contrib import admin

# Register your models here.
from .models import TiposExames, PedidosExames, SolicitacaoExame

admin.site.register(TiposExames)
admin.site.register(PedidosExames)
admin.site.register(SolicitacaoExame)