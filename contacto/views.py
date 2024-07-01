from django.shortcuts import render
from .forms import contactoForm

def contacto(request):
    data = {
        'form': contactoForm()
    }
    if request.method == 'POST':
        formulario = contactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else: 
            data["form"] = formulario
    return render(request,"contacto/contacto.html",data)

# Create your views here.
