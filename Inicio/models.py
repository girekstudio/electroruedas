from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Marca_Electroruedas(models.Model):
    favicon_color = models.ImageField(upload_to='favicon', help_text='imagenes 20*20')
    logo_horizontal = models.ImageField(upload_to='favicon',null=True, blank=True, help_text='imagenes 20*20')

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.logo_horizontal)


    class Meta:
        verbose_name_plural = "1. Electroruedas"


class Slider(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    detalle= models.TextField(max_length=100, null=True, blank=True)
    imagen=models.ImageField(upload_to='media', null=True, blank=True, help_text='imagenes 500*900')

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>"%self.imagen)


    class Meta:
        verbose_name_plural = "2. Slider"

class Electroruedas_galeria(models.Model):
    imag_fondo_ventajas = models.ImageField(upload_to='electroruedas', null=True, blank=True, help_text='Inicio - Seccion Ventajas imagenes 300*900')
    imag_empresa = models.ImageField(upload_to='electroruedas', null=True, blank=True, help_text='Empresa - Seccion Quienes somos imagenes 300*500')
    imag_ventaja_01 = models.ImageField(upload_to='electroruedas', null=True, blank=True, help_text='Empresa - Seccion Ventaja 300*500')
    imag_ventaja_02 = models.ImageField(upload_to='electroruedas', null=True, blank=True, help_text='Empresa - Seccion Ventaja 300*500')
    imag_ventaja_03 = models.ImageField(upload_to='electroruedas', null=True, blank=True, help_text='Empresa - Seccion Ventaja 300*500')
    imagen_2=models.ImageField(upload_to='media', null=True, blank=True, help_text='imagenes 500*900')
    imagen_3=models.ImageField(upload_to='media', null=True, blank=True, help_text='imagenes 500*900')
    imagen_4=models.ImageField(upload_to='media', null=True, blank=True, help_text='imagenes 500*900')
    imagen_5=models.ImageField(upload_to='media', null=True, blank=True, help_text='imagenes 500*900')
    imagen_6 = models.ImageField(upload_to='media', null=True, blank=True, help_text='imagenes 500*900')
    imagen_7 = models.ImageField(upload_to='media', null=True, blank=True, help_text='imagenes 500*900')
    imagen_8 = models.ImageField(upload_to='media', null=True, blank=True, help_text='imagenes 500*900')
    imagen_9 = models.ImageField(upload_to='media', null=True, blank=True, help_text='imagenes 500*900')


    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>"%self.imag_empresa)


    class Meta:
        verbose_name_plural = "3. Inicio"

class Empresa(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    nosotros = models.TextField(max_length=500, null=True, blank=True)
    quienes_somos = models.TextField(max_length=500, null=True, blank=True)
    titulo_marcas = models.TextField(max_length=500, null=True, blank=True)
    sub_titulo_marcas = models.TextField(max_length=500, null=True, blank=True)
    titulo_ventajas = models.TextField(max_length=500, null=True, blank=True)
    titulo_2 = models.TextField(max_length=500, null=True, blank=True)
    sub_titulo_2 = models.TextField(max_length=500, null=True, blank=True)
    titulo_3 = models.TextField(max_length=500, null=True, blank=True)
    sub_titulo_3 = models.TextField(max_length=500, null=True, blank=True)
    titulo_4 = models.TextField(max_length=500, null=True, blank=True)
    sub_titulo_4 = models.TextField(max_length=500, null=True, blank=True)
    titulo_5 = models.TextField(max_length=500, null=True, blank=True)
    sub_titulo_5 = models.TextField(max_length=500, null=True, blank=True)
    titulo_6 = models.TextField(max_length=500, null=True, blank=True)
    sub_titulo_6 = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name_plural = "4. Empresa"


class Valor(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    detalle = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name_plural = "5. Valor"


class Beneficios(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "6. Beneficios"



class Ventajas(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    detalle = models.TextField(max_length=500, null=True, blank=True)


    class Meta:
        verbose_name_plural = "6. Ventajas"


class Articulo_diario(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    imagen = models.ImageField(upload_to='articulo', null=True, blank=True, help_text='imagenes 500*900')
    parrafo_1 = models.TextField(max_length=1500, null=True, blank=True)
    parrafo_2 = models.TextField(max_length=1500, null=True, blank=True)
    link = models.CharField(max_length=800, null=True, blank=True)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>"%self.imagen)

    class Meta:
        verbose_name_plural = "5. Articulo Diario"


class Contacto_electroruedas(models.Model):
    whatsapp = models.CharField(max_length=13, null=True, blank=True)
    celular_1 = models.CharField(max_length=11, null=True, blank=True)
    celular_2 = models.CharField(max_length=100, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    horario_lu_vier = models.CharField(max_length=100, null=True, blank=True)
    horario_sab = models.CharField(max_length=100, null=True, blank=True)
    horario_dom = models.CharField(max_length=100, null=True, blank=True)



    class Meta:
        verbose_name_plural = "7. Contacto ElecctroRuedas"



class Contacto_redes(models.Model):
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    behance = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "8. Contácto Redes Sociales"