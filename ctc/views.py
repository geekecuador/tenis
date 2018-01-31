from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Categoria, Publicacion, Circular

# Create your views here.


def publicacion(request, idpost):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    publicacion = Publicacion.objects.get(id=idpost)
    return render(request, 'publicacion.html',{
        "publicacion": publicacion,"publicaciones":publicaciones
    })

def mensaje(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        asunto = request.POST['asunto']
        mensaje = request.POST['mensaje']
        send_mail(
        asunto,
        mensaje + " de parte de: "+nombre+" con email: "+email,
        'correo@cotopaxitenisclub.com',
        ['correo@cotopaxitenisclub.com'],
        fail_silently=False,)
        publicaciones = Publicacion.objects.order_by("-fecha")[:5]
        return render(request, 'mensaje.html', {"publicaciones": publicaciones})
    else:
        return redirect('/')


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
