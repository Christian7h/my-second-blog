from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

class BlogPost(models.Model):
    title=models.CharField(max_length=255)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.CharField(max_length=130)
    text = RichTextField(_('text'))
    description = models.TextField(_('description'), default='Default description')
    content=models.TextField()
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    dateTime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) +  " Blog Title: " + self.title
    
    def get_absolute_url(self):
        return reverse('blogs')
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
    dateTime=models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username +  " Comment: " + self.content


class CarouselImage(models.Model):
    title = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='carousel/')
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):

        return self.title
    
class Servicio(models.Model):
    titulo = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='servicios/')
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
    
class ReservaCita(models.Model):
    nombre_profesional = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='reservaCita/')
    google_calendar_url = models.URLField()
    color = models.CharField(max_length=7)  # Color en formato hexadecimal (#RRGGBB)
    etiqueta_boton = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_profesional

class Profesional(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='profesionales/')
    especialidades = models.TextField()

    def obtener_especialidades(self):
        return self.especialidades.split('\n')

    def __str__(self):
        return self.nombre