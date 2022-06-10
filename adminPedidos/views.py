from django.shortcuts import render
from adminPedidos.models import *
from adminPedidos.formularios import *
from django.http import HttpResponse

# Create your views here.
def error_404(request, exception):
    return render(request, "Error/404.html",{})


def busqueda_articulos(request):
    mensaje = "No has realizado una busqueda."
    articulos = []
    if request.method == "GET":
        busqueda = request.GET.get("txtBusqueda", "")
        if busqueda:
            mensaje = "Articulo buscado: %s" % busqueda
            articulos = Articulo.objects.filter(nombre__icontains=busqueda)
            mensaje = "Se ha encontrado esto en su busqueda."
    return render(request, "buscar_articulos.html", {"msj":mensaje, "articulos":articulos})


def nuevo_articulo(request):
    mensaje = "Aqui podras agregar nuevos articulos."
    if request.method == "POST":
        articuloFormulario = ArticuloFormulario(request.POST)
        if articuloFormulario.is_valid():
            nombre = articuloFormulario.cleaned_data.get("nombre", "")
            precio = articuloFormulario.cleaned_data.get("precio", "")
            tipo = articuloFormulario.cleaned_data.get("tipo", "")
            #tipo2 = articuloFormulario.cleaned_data.get("tipo2")
            a = Articulo(nombre=nombre, precio=precio, tipo=TipoArticulo.objects.get(id=tipo))
            a.save()
            #return HttpResponse("El articulo se ha agregado correctamente")
            articuloFormulario = ArticuloFormulario()
            mensaje = "El articulo se ha agregado correctamente."
    else:
            articuloFormulario = ArticuloFormulario()
    return render(request, "nuevo_articulo.html", {"form": articuloFormulario, "msj":mensaje})

def modificar_articulo(request, id):
    id_articulo= Articulo.objects.get(id=id)
    if request.method == "POST":
        articuloFormulario = ArticuloFormulario(request.POST)
        if articuloFormulario.is_valid():
            nombre = articuloFormulario.cleaned_data.get("nombre", "")
            precio = articuloFormulario.cleaned_data.get("precio", "")
            tipo = articuloFormulario.cleaned_data.get("tipo", "")

            id_articulo.nombre = nombre
            id_articulo.precio = precio
            id_articulo.tipo = TipoArticulo.objects.get(id=tipo)
            id_articulo.save()
            return HttpResponse("El articulo se ha modificado correctamente")
    else:
        dict_articulo={"nombre": id_articulo.nombre,
                       "precio": id_articulo.precio,
                       "tipo": id_articulo.tipo.id
        }
        articuloFormulario = ArticuloFormulario(dict_articulo)
    return render(request, "modificar_articulo.html", {"form": articuloFormulario})

def eliminar_articulo(request, id):
    id_articulo = Articulo.objects.get(id=id)
    if request.method == "POST":
        if id_articulo:
            id_articulo.delete()
            return HttpResponse("El articulo se ha eliminado correctamente")
    else:
        dict_articulo = {"nombre": id_articulo.nombre,
                         "precio": id_articulo.precio,
                         "tipo": id_articulo.tipo.id
                         }
        articuloFormulario = ArticuloFormulario(dict_articulo)
    return render(request, "eliminar_articulo.html", {"form": articuloFormulario})
