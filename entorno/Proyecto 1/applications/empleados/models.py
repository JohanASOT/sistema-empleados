from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField(verbose_name='Habilidades', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return f"{self.id}. {self.habilidad}"

JOB_CHOICES = (
    ('0', 'Contador'),
    ('1', 'Administrador'),
    ('2', 'Economista'),
    ('3', 'Otro')
)

class Empleado(models.Model):
    first_name = models.CharField(verbose_name='Nombres', max_length=60)
    last_name = models.CharField(verbose_name='Apellidos', max_length=60)
    full_name = models.CharField(verbose_name='Nombre Completo', max_length=120, blank=True)
    job = models.CharField(verbose_name='Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    avatar = models.ImageField(verbose_name='Imagen', upload_to='empleados', blank=True, null=True)
    hoja_vida = RichTextField(default=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        # Puedo ordenar tanto en views.py como en models.py


    def __str__(self):
        return f"{self.id}. {self.first_name} {self.last_name}"
