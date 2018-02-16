from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Categoria, Publicacion, Circular

# Create your views here.


def publicacion(request, idpost):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    publicacion = Publicacion.objects.get(id=idpost)
    return render(request, 'publicacion.html',{
        "publicacion": publicacion,"publicaciones":publicaciones,"circular":circular
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
        ['administracion@cotopaxitenisclub.com','cotopaxitenisclub@gmail.com'],
        fail_silently=False,)
        publicaciones = Publicacion.objects.order_by("-fecha")[:5]
        circular = Circular.objects.get(titulo='circular')
        return render(request, 'mensaje.html', {"publicaciones": publicaciones,"circular":circular})
    else:
        return redirect('/')


def index(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    return render(request, 'index.html', {"publicaciones":publicaciones,"circular":circular})


def contacto(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    return render(request, 'contacto.html', {"publicaciones":publicaciones,"circular":circular})

def blog(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    return render(request, 'blog.html', {"publicaciones":publicaciones,"circular":circular})

def cotopaxi(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    return render(request, 'cotopaxi.html', {"publicaciones":publicaciones,"circular":circular})


def daviscup(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    return render(request, 'daviscup.html', {"publicaciones":publicaciones,"circular":circular})


def directorio(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    return render(request, 'directorio.html', {"publicaciones":publicaciones,"circular":circular})


def dobles(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    return render(request, 'dobles.html', {"publicaciones":publicaciones,"circular":circular})


def estatutos(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    return render(request, 'estatutos.html', {"publicaciones":publicaciones,"circular":circular})


def eventos(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    return render(request, 'eventos.html', {"publicaciones":publicaciones,"circular":circular})


def historia(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    return render(request, 'historia.html', {"publicaciones":publicaciones,"circular":circular})


def master(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    return render(request, 'master.html', {"publicaciones":publicaciones,"circular":circular})


def presidentes(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    return render(request, 'presidentes.html', {"publicaciones":publicaciones,"circular":circular})


def ranking(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    return render(request, 'ranking.html', {"publicaciones":publicaciones,"circular":circular})


def reinas(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    return render(request, 'reinas.html', {"publicaciones":publicaciones,"circular":circular})


def tenis(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    return render(request, 'tenis.html', {"publicaciones":publicaciones,"circular":circular})

def instalaciones(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    return render(request, 'instalaciones.html', {"publicaciones":publicaciones,"circular":circular})




def contacto(request):
    publicaciones = Publicacion.objects.order_by("-fecha")[:5]
    circular = Circular.objects.get(titulo='circular')
    return render(request, 'contacto.html', {"publicaciones":publicaciones,"circular":circular})
