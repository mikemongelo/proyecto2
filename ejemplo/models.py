from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from django.db.models.fields import URLField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User

class Noticia(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_de_creacion = models.DateTimeField(default=timezone.now)
    fecha_de_publicacion = models.DateTimeField(blank=True, null=True)
    imagen = models.ImageField(upload_to = 'imagenes/',null=True,blank=True)    
    
    def publish(self):
        self.fecha_de_publicacion = timezone.now()
        self.save()
 
    def __str__(self):
        return self.titulo    

      

class Comentario(models.Model):
    dni = models.IntegerField(blank=True, null=True)
    apellido = models.CharField(max_length=50,blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=100,null=False,blank=False)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    textoComentario = models.TextField(blank=False, null=False)
    fechaComentario = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre + ' '  + self.apellido
        

class Video(models.Model):
    id = models.CharField(max_length=20,primary_key = True)
    url = URLField(null=True)
    titulo = models.CharField(max_length = 50)
    descripcion = models.TextField()

class  Historia(models.Model):
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    historia = models.TextField()
    imagen = models.ImageField(upload_to = 'imagenes/', null=True, blank=True)  

    def GetNombre(self):
        return self.nombre + ' ' + self.apellido 


class Equipo(models.Model):
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    comentario = models.TextField(max_length = 200)
    imagen = models.ImageField(upload_to = 'imagenes/', null=True, blank=True)  
    def SuNombreEs(self):
        return self.nombre + ' ' + self.apellido 


class GaleriaFoto(models.Model):
    descripcion = models.CharField(max_length = 40)
    imagen = models.ImageField(upload_to = 'imagenes/', null=True, blank=True)

class ComentarioPosteo(models.Model):
    posteo = models.ForeignKey('Noticia',on_delete=models.CASCADE)
    creador = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cuerpo  = models.TextField(max_length = 300)
    fechacreacion = models.DateTimeField(auto_now_add=True, null=True)

# Create your models 
# here.
