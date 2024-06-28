from django.shortcuts import render, get_object_or_404
from .models import Comic


def catalogo(request):
    comics = Comic.objects.all()
    for comic in comics:
        comic.precio_clp = "{:,}".format(comic.precio) 
    context = {"comics":comics}
    return render(request, "comics/catalogo.html",context)

def home(request):

    dc_comics = Comic.objects.filter(id_categoria__categoria='dc')
    marvel_comics = Comic.objects.filter(id_categoria__categoria='marvel')
    manga_comics = Comic.objects.filter(id_categoria__categoria='manga')
    ultimos_comics = Comic.objects.all().order_by('-id')[:6]

    for comic in ultimos_comics:
        comic.precio_clp = "{:,}".format(comic.precio)
    for comic in marvel_comics:
        comic.precio_clp = "{:,}".format(comic.precio)
    for comic in dc_comics:
        comic.precio_clp = "{:,}".format(comic.precio)
    for comic in manga_comics:
        comic.precio_clp = "{:,}".format(comic.precio)

    context = {
        'dc_comics': dc_comics,
        'marvel_comics': marvel_comics,
        'manga_comics': manga_comics,
        'ultimos_comics': ultimos_comics,
    }
    return render(request, 'comics/home.html', context)


def detallesComic(request, id):
        comic = get_object_or_404(Comic, id=id)
        comic.precio_clp = "{:,}".format(comic.precio) 
        context = {"comic":comic}
        return render(request, "comics/detallesComic.html", context)

def comicsCarro(request):
    
    comicscarro = Comic.objects.all()#Este es el select * from
    context = {"comicscarro":comicscarro}
    return render(request,"carrito/carrito.html",context)    
        

# Create your views here.
