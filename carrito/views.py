from django.shortcuts import render, redirect, get_object_or_404
from .carrito import Carrito
from comics.models import Comic
    


def index(request):
    carro = Carrito(request)
    context = {'carro': carro.carro,
              'user_authenticated': request.user.is_authenticated, }
    return render(request, "carrito/carrito.html", context)


def agregarCarro(request, comic_id):
    carro = Carrito(request)
    comic = get_object_or_404(Comic, id=comic_id)
    carro.agregar(comic=comic)
    return redirect("carro:carrito")


def eliminarCarro(request, comic_id):
    carro = Carrito(request)
    comic = get_object_or_404(Comic, id=comic_id)
    carro.eliminar(comic=comic)
    return redirect("carro:carrito")

def limpiarCarro(request):
    carro = Carrito(request)
    carro.limpiar()
    return redirect("carro:carrito")

