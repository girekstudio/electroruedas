from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Electroruedas(models.Model):
    favicon_blanco=models.ImageField(upload_to='favicon', help_text='imagenes 20*20')
    favicon_color = models.ImageField(upload_to='favicon', help_text='imagenes 20*20')
    logo_horizontal = models.ImageField(upload_to='favicon',null=True, blank=True, help_text='imagenes 20*20')
    logo_horizontal_blanco = models.ImageField(upload_to='favicon',null=True, blank=True, help_text='imagenes 20*20')
    logo = models.ImageField(upload_to='favicon', help_text='imagenes 20*20')
    logo_blanco= models.ImageField(upload_to='favicon', help_text='imagenes 20*20')

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.logo_horizontal)


    class Meta:
        verbose_name_plural = "1. Electroruedas"


class Slider(models.Model):
    imagen=models.ImageField(upload_to='media', null=True, blank=True, help_text='imagenes 500*900')

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>"%self.imagen)


    class Meta:
        verbose_name_plural = "2. Slider"

class Electroruedas_galeria(models.Model):
    imagen_1=models.ImageField(upload_to='media', null=True, blank=True, help_text='imagenes 500*900')
    imagen_2=models.ImageField(upload_to='media', null=True, blank=True, help_text='imagenes 500*900')
    imagen_3=models.ImageField(upload_to='media', null=True, blank=True, help_text='imagenes 500*900')
    imagen_4=models.ImageField(upload_to='media', null=True, blank=True, help_text='imagenes 500*900')
    imagen_5=models.ImageField(upload_to='media', null=True, blank=True, help_text='imagenes 500*900')

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>"%self.imagen_1)


    class Meta:
        verbose_name_plural = "3. Inicio"

class Empresa(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    nosotros = models.TextField(max_length=500, null=True, blank=True)
    mision = models.TextField(max_length=500, null=True, blank=True)
    vision = models.TextField(max_length=500, null=True, blank=True)
    valor_1 = models.TextField(max_length=500, null=True, blank=True)
    valor_2 = models.TextField(max_length=500, null=True, blank=True)
    valor_3 = models.TextField(max_length=500, null=True, blank=True)
    valor_4 = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name_plural = "4. Empresa"





class Contacto_electroruedas(models.Model):
    whatsapp = models.CharField(max_length=13, null=True, blank=True)
    celular_1 = models.CharField(max_length=11, null=True, blank=True)
    celular_2 = models.CharField(max_length=100, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)


    class Meta:
        verbose_name_plural = "6. Contacto ElecctroRuedas"



class Contacto_redes(models.Model):
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    behance = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "7. Contácto Redes Sociales"