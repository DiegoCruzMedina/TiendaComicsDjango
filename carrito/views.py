from django.shortcuts import render, redirect, get_object_or_404
from .carrito import Carrito
from comics.models import Comic
from ordenes.models import Orden, ItemOrden
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#se realizara una unica vez la transaccion, si este falla se revertira, asegura datos
from django.db import transaction    


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

def restarCarro(request,comic_id):
    carro= Carrito(request)
    comic= get_object_or_404(Comic, id=comic_id)
    carro.restar(comic=comic)
    return redirect("carro:carrito")

@login_required
def comprarCarro(request):
    if request.user.is_authenticated:
        carro = Carrito(request)
        total_precio = sum(float(item['precio']) for item in carro.carro.values())
        cantidad_comics = sum(item['cantidad'] for item in carro.carro.values())
        
        # Verificar si hay suficiente cantidad disponible para todos los cómics en el carrito
        for key, value in carro.carro.items():
            comic = Comic.objects.get(id=key)
            if comic.cantidad < value['cantidad']:
                messages.error(request, f"No hay suficiente cantidad de {comic.nombre} disponible.")
                return redirect("carro:carrito")

        with transaction.atomic():
            # Crear la orden
            orden = Orden.objects.create(
                usuario=request.user,
                total_precio=total_precio,
                cantidad_comics=cantidad_comics
            )

            # Crear los items de la orden y actualizar la cantidad de cómics
            for key, value in carro.carro.items():
                comic = Comic.objects.get(id=key)
                ItemOrden.objects.create(
                    orden=orden,
                    comic_id=key,
                    cantidad=value['cantidad'],
                    precio=value['precio']
                )
                # Actualizar la cantidad de cómics disponibles
                comic.cantidad -= value['cantidad']
                comic.save()

            carro.limpiar()
            messages.success(request, "Compra realizada exitosamente")
            return redirect("carro:carrito")
    else:
        messages.error(request, "Debes iniciar sesión para realizar la compra")
        return redirect("login")



def limpiarCarro(request):
    carro = Carrito(request)
    carro.limpiar()
    return redirect("carro:carrito")
    

