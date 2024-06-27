from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class VRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registro/registro.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro/registro.html", {"form": form})

def close_session(request):
    logout(request)
    return redirect('home')

def logear(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")
    return render(request, "login/login.html", {"form": form})

# Create your views here.
