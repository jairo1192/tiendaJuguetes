from django import forms

from adminPedidos.models import *


tipo_articulos = TipoArticulo.objects.all()
choices_articulos = []
for item in tipo_articulos:
    choices_articulos.append((item.id, item.nombre))
choices_articulos = tuple(choices_articulos)

class ArticuloFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    precio = forms.FloatField()
    tipo = forms.ChoiceField(choices=choices_articulos)
