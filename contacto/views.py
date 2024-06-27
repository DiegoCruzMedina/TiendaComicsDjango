from django.shortcuts import render


def index(request):
    context = {}
    return render(request,"contacto/contacto.html",context)
# Create your views here.
