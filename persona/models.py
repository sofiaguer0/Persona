from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class persona(models.Model):
    apellido = models.CharField(max_length=30)
    nombre = models.CharField( max_length=40)
    dni = models.CharField(max_length=8, verbose_name='D.N.I')
    email = models.EmailField(max_length=250, unique=True,null=False,blank=False)
    vive = models.BooleanField(default=True)
    fecha_nac = models.DateField(verbose_name= "Fecha nacimiento")
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateField(auto_now_add = True)
    legajo = RichTextField(default ='legajo')
    class meta:
        verbose_name = 'persona'
        verbose_name_plural='personas'

    def __str__(self):
        return f'{self.apellido},{self.nombre}'
    
    
class contacto(models.Model):
    nombre = models.CharField(max_length=60)
    email = models.CharField(max_length=250)
    mensaje = models.TextField(max_length=300)
    
    







