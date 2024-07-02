from django.db import models

# Create your models here.

class Prueba(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=30)
    subtitle = models.CharField(verbose_name='Subtitulo', max_length=50)
    cantidad = models.IntegerField(verbose_name='Cantidad')

    def __str__(self):
        return f"{self.id}. {self.title} - {self.subtitle}"