from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def contacto(request):
    return render(request, 'contacto.html', {})


def cotopaxi(request):
    return render(request, 'cotopaxi.html', {})


def daviscup(request):
    return render(request, 'daviscup.html', {})


def directorio(request):
    return render(request, 'directorio.html', {})


def dobles(request):
    return render(request, 'dobles.html', {})


def estatutos(request):
    return render(request, 'estatutos.html', {})


def eventos(request):
    return render(request, 'eventos.html', {})


def historia(request):
    return render(request, 'historia.html', {})


def master(request):
    return render(request, 'master.html', {})


def presidentes(request):
    return render(request, 'presidentes.html', {})


def ranking(request):
    return render(request, 'ranking.html', {})


def reinas(request):
    return render(request, 'reinas.html', {})


def tenis(request):
    return render(request, 'tenis.html', {})


def contacto(request):
    return render(request, 'contacto.html', {})
