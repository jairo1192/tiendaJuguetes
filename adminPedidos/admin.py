from django.contrib import admin

# Register your models here.
from adminPedidos.models import *

class tipoArticuloAdmin(admin.ModelAdmin):
    list_display = ["nombre"]

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "tipo"]
    ordering = ["nombre","precio"]
    search_fields = ["nombre"]

class PedidosAdmin(admin.ModelAdmin):
    list_display = ["numero_pedido", "fecha"]
    list_filter = ["fecha"]
    date_hierarchy = "fecha"

admin.site.register(TipoArticulo, tipoArticuloAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Pedidos, PedidosAdmin)