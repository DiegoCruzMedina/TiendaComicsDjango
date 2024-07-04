from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Orden

@login_required
def mis_pedidos(request):
    pedidos = Orden.objects.filter(usuario=request.user)
    context = {
        'pedidos': pedidos
    }
    return render(request, 'ordenes/misPedidos.html', context)
