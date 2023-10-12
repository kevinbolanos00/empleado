from email.mime import image
from django.db import models
from aplications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.
class Habilidades(models.Model):
   habilidad = models.CharField('Habilidad', max_length=50)
   class meta:
     verbose_name='Habilidad'
     verbose_name_plural = 'Habilidades empleado'



   def __str__(self) :
        return str(self.id) + '-' + self.habilidad


class Empleado(models.Model):
    """Modelo para la tabla Empleado"""
    JOB_CHOISES=(
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('3', 'ECONOMISTA'),
        ('4', 'OTRO'),
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('apellidos', max_length=60)
    full_name= models.CharField('nombres completos', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOISES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True) 
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
     verbose_name='Mis empleados'
     verbose_name_plural = 'Mis colaboradores'
     ordering = ['last_name']
     #unique_together = ('name', 'shor_name')



    def __str__(self) :
        return str(self.id) + '-' + self.first_name + '-' + self.last_name 
    

        
