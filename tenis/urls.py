"""tenis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from ctc import views
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index, name='index'),
                  path('historia', views.historia, name='historia'),
                  path('contacto', views.contacto, name='contacto'),
                  path('instalaciones', views.instalaciones, name='instalaciones'),
                  path('cotopaxi', views.cotopaxi, name='cotopaxi'),
                  path('daviscup', views.daviscup, name='daviscup'),
                  path('directorio', views.directorio, name='directorio'),
                  path('dobles', views.dobles, name='dobles'),
                  path('estatutos', views.estatutos, name='estatutos'),
                  path('eventos', views.eventos, name='eventos'),
                  path('master', views.master, name='master'),
                  path('presidentes', views.presidentes, name='presidentes'),
                  path('ranking', views.ranking, name='ranking'),
                  path('reinas', views.reinas, name='reinas'),
                  path('tenis', views.tenis, name='tenis'),
                  path('blog', views.blog, name='blog'),
                  path('mensaje', views.mensaje, name='mensaje'),
                  path('publicacion/<int:idpost>', views.publicacion, name='publicacion'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
