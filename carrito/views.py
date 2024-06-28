from django.shortcuts import render, redirect
from .carrito import Carrito
from comics.models import Comic

def index(request):
    context = {}
    return render(request, "carrito/carrito.html", context)

def agregarCarro(request, comic_id):
    carro = Carrito(request)
    comic = Comic.objects.get(id=comic_id)
    imagen_url = comic.imagen
    print(carro)

    carro.agregar(comic=comic)
    return redirect("carro:carrito")  # Usando el namespace y nombre de la vista


# Create your views here.
