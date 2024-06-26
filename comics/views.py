from django.shortcuts import render
from .models import Comic

def index(request):
    comics = Comic.objects.all()
    context = {"comics":comics}
    return render(request, "comics/index.html",context)

# Create your views here.
