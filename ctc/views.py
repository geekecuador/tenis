from django.shortcuts import render
from .models import Categoria, Publicacion

# Create your views here.


def publicacion(request, idpost):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    publicacion = Publicacion.objects.get(id=idpost)
    return render(request, '',{
        "publicacion": publicacion,"publicaciones":publicaciones
    })

def index(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    return render(request, 'index.html', {"publicaciones":publicaciones})


def contacto(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    return render(request, 'contacto.html', {"publicaciones":publicaciones})

def blog(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    return render(request, 'blog.html', {"publicaciones":publicaciones})

def cotopaxi(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    return render(request, 'cotopaxi.html', {"publicaciones":publicaciones})


def daviscup(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    return render(request, 'daviscup.html', {"publicaciones":publicaciones})


def directorio(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    return render(request, 'directorio.html', {"publicaciones":publicaciones})


def dobles(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    return render(request, 'dobles.html', {"publicaciones":publicaciones})


def estatutos(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    return render(request, 'estatutos.html', {"publicaciones":publicaciones})


def eventos(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    return render(request, 'eventos.html', {"publicaciones":publicaciones})


def historia(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    return render(request, 'historia.html', {"publicaciones":publicaciones})


def master(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    return render(request, 'master.html', {"publicaciones":publicaciones})


def presidentes(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    return render(request, 'presidentes.html', {"publicaciones":publicaciones})


def ranking(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    return render(request, 'ranking.html', {"publicaciones":publicaciones})


def reinas(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    return render(request, 'reinas.html', {"publicaciones":publicaciones})


def tenis(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    return render(request, 'tenis.html', {"publicaciones":publicaciones})


def contacto(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    return render(request, 'contacto.html', {"publicaciones":publicaciones})
