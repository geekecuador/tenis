from django.db import models

# Create your models here.
class Categoria(models.Model):
    name = models.CharField(max_length=200)

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='imagenes/')
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria,  on_delete='cascade')
    fecha = models.DateTimeField(auto_now_add=True)