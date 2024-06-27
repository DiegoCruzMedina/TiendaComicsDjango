from django.shortcuts import render


def index(request):
    context = {}
    return render(request,"carrito/carrito.html",context)
# Create your views here.
