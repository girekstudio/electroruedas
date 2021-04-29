from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

class Marcas(models.Model):
    titulo=models.CharField(max_length=50, null=True, blank=True)
    logo = models.ImageField(upload_to='marca', null=True, blank=True, help_text='360x360')

    def __str__(self):
        return '%s' % (self.titulo)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.logo)


    class Meta:
        verbose_name_plural = "1. Marcas "

class Tipo_producto(models.Model):
    icono = models.ImageField(upload_to='media', null=True, blank=True, help_text='360x360')
    titulo=models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.titulo)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.icono)



    class Meta:
        verbose_name_plural = "2. Tipo de producto "


class Product(models.Model):
    offer = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    stock = models.BooleanField(default=True)
    tipo_producto = models.ForeignKey(Tipo_producto, on_delete=models.CASCADE, null=True, blank=True )
    titulo=models.CharField(max_length=50, null=True, blank=True)
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE, null=True, blank=True )
    velocidad = models.CharField(max_length=50, null=True, blank=True)
    autonomia = models.CharField(max_length=50, null=True, blank=True)
    motor = models.CharField(max_length=50, null=True, blank=True)
    bateria = models.CharField(max_length=50, null=True, blank=True)
    tiempo_carga  = models.CharField(max_length=50, null=True, blank=True)
    carga_maxima = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.TextField(max_length=500, null=True, blank=True)
    precio = models.DecimalField(max_digits=999, decimal_places=2)
    precio_oferta = models.DecimalField(max_digits=999, decimal_places=2, null=True, blank=True)
    imagen_1 = models.ImageField(upload_to='media', null=True, blank=True, help_text='360x360')
    imagen_2 = models.ImageField(upload_to='media', null=True, blank=True, help_text='360x360')
    imagen_3 = models.ImageField(upload_to='media', null=True, blank=True, help_text='360x360')
    imagen_4 = models.ImageField(upload_to='media', null=True, blank=True, help_text='360x360')
    imagen_5 = models.ImageField(upload_to='media', null=True, blank=True, help_text='360x360')
    imagen_6 = models.ImageField(upload_to='media', null=True, blank=True, help_text='360x360')
    blanco = models.BooleanField(default=False)
    gris = models.BooleanField(default=False)
    negro = models.BooleanField(default=False)
    rojo = models.BooleanField(default=False)
    amarillo = models.BooleanField(default=False)
    azul = models.BooleanField(default=False)
    celeste = models.BooleanField(default=False)
    verde = models.BooleanField(default=False)
    turquesa = models.BooleanField(default=False)
    violeta = models.BooleanField(default=False)
    cafe = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return '%s' % (self.titulo)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>" % self.imagen_1)



    class Meta:
        verbose_name_plural = "3. Producto "
