from django.contrib import admin
admin.site.site_header = "Sitio web de Administración Utopy Toys"
admin.site.site_title = "Portal de Administradores"
admin.site.index_title = "Bienvenido al Portal de Administrador"

# Register your models here.
from .models import Articulo
from adminPedidos.models import *

class tipoArticuloAdmin(admin.ModelAdmin):
    list_display = ["nombre"]

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "tipo"]
    ordering = ["nombre","precio"]
    search_fields = ["nombre"]
    fields = ("nombre", "precio", "tipo")

class PedidosAdmin(admin.ModelAdmin):
    list_display = ["numero_pedido", "fecha"]
    list_filter = ["fecha"]
    date_hierarchy = "fecha"

class DevolucionesAdmin(admin.ModelAdmin):
    list_display = ["numero_pedido", "fecha"]
    list_filter = ["fecha"]
    date_hierarchy = "fecha"

class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ["nombre_empresa", "direccion","email","telefono", "persona_contacto", "numero_identificacion_fiscal"]
    list_filter = ["nombre_empresa", "numero_identificacion_fiscal"]
    search_fields = ["nombre_empresa"]

class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "direccion","email","telefono"]
    list_filter = ["nombre", "email", "telefono"]
    search_fields = ["nombre"]


admin.site.register(TipoArticulo, tipoArticuloAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Pedidos, PedidosAdmin)
admin.site.register(Devoluciones, DevolucionesAdmin)
admin.site.register(Proveedores, ProveedoresAdmin)
admin.site.register(Cliente, ClienteAdmin)