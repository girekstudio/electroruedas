from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Clientes(models.Model):
    nombre = models.CharField(max_length=30, null=True, blank=True)
    foto = models.ImageField(upload_to='clientes', null=True, blank=True, help_text='100x100')




    def __str__(self):
        return '%s' % (  self.nombre)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.foto)



    class Meta:
        verbose_name_plural = "1. Clientes "

