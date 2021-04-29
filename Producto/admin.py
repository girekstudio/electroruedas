from django.contrib import admin

# Register your models here.
from Producto.models import *
from electroruedas.snippers import Attr


@admin.register(Marcas)
class MarcasAdmin(admin.ModelAdmin):
    list_display = Attr(Marcas)+["miniatura"]
    list_display_links = Attr(Marcas)

@admin.register(Tipo_producto)
class ProductAdmin(admin.ModelAdmin):
    list_display = Attr(Tipo_producto)+["miniatura"]
    list_display_links = Attr(Tipo_producto)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = Attr(Product)+["miniatura"]
    list_display_links = Attr(Product)


