from colorfield.fields import ColorField
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

from electroruedas.snippers import ResizeImageMixin


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
    icono =models.CharField(max_length=50, null=True, blank=True)
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
    dimensiones = models.CharField(max_length=100, null=True, blank=True)
    distancia_ejes = models.CharField(max_length=100, null=True, blank=True)
    controlador = models.CharField(max_length=100, null=True, blank=True)
    frenos = models.CharField(max_length=100, null=True, blank=True)
    dimensiones_rueda = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField(max_length=500, null=True, blank=True)
    precio = models.DecimalField(max_digits=999, decimal_places=2)
    precio_oferta = models.DecimalField(max_digits=999, decimal_places=2, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.titulo)




    class Meta:
        verbose_name_plural = "3. Producto "


class Imagen_product(models.Model, ResizeImageMixin):
    producto=models.ForeignKey(Product, on_delete=models.CASCADE,)
    imagen= models.ImageField(upload_to='producto', null=True, blank=True, help_text='360x360')
    color=ColorField(default="#ffff")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.resize(self.imagen, (600, 600))
        super(Imagen_product, self).save()

    def delete(self, using=None, keep_parents=False):
        storage, path = self.imagen.storage, self.imagen.path
        super(Imagen_product, self).delete()
        storage.delete(path)

    class Meta:
        verbose_name_plural = "4. Imagenes de Producto "


class Galeria_product(models.Model):
    producto=models.ForeignKey(Product, on_delete=models.CASCADE,)
    imagen= models.ImageField(upload_to='producto', null=True, blank=True, help_text='360x360')


    class Meta:
        verbose_name_plural = "5. Galerìa de Producto "


