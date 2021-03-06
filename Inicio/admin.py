from django.contrib import admin

# Register your models here.
from Inicio.models import *
from electroruedas.snippers import Attr


@admin.register(Marca_Electroruedas)
class Marca_ElectroruedasAdmin(admin.ModelAdmin):
    list_display = Attr(Marca_Electroruedas)+["miniatura"]
    list_display_links = Attr(Marca_Electroruedas)

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = Attr(Slider)+["miniatura"]
    list_display_links = Attr(Slider)

@admin.register(Electroruedas_galeria)
class Electroruedas_galeriaAdmin(admin.ModelAdmin):
    list_display = Attr(Electroruedas_galeria)+["miniatura"]
    list_display_links = Attr(Electroruedas_galeria)

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = Attr(Empresa)
    list_display_links = Attr(Empresa)


@admin.register(Valor)
class ValorAdmin(admin.ModelAdmin):
    list_display = Attr(Valor)
    list_display_links = Attr(Valor)

@admin.register(Beneficios)
class BeneficiosAdmin(admin.ModelAdmin):
    list_display = Attr(Beneficios)
    list_display_links = Attr(Beneficios)

@admin.register(Ventajas)
class BeneficiosAdmin(admin.ModelAdmin):
    list_display = Attr(Ventajas)
    list_display_links = Attr(Ventajas)

@admin.register(Articulo_diario)
class Articulo_diarioAdmin(admin.ModelAdmin):
    list_display = Attr(Articulo_diario)+["miniatura"]
    list_display_links = Attr(Articulo_diario)

@admin.register(Contacto_electroruedas)
class Contacto_electroruedasAdmin(admin.ModelAdmin):
    list_display = Attr(Contacto_electroruedas)
    list_display_links = Attr(Contacto_electroruedas)

@admin.register(Contacto_redes)
class Contacto_redesAdmin(admin.ModelAdmin):
    list_display = Attr(Contacto_redes)
    list_display_links = Attr(Contacto_redes)

@admin.register(Envio_Email)
class Envio_EmailsAdmin(admin.ModelAdmin):
    list_display = Attr(Envio_Email)
    list_display_links = Attr(Envio_Email)

@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = Attr(Promo)
    list_display_links = Attr(Promo)