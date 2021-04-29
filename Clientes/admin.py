from django.contrib import admin

# Register your models here.
from Clientes.models import *
from electroruedas.snippers import Attr


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = Attr(Clientes)+["miniatura"]
    list_display_links = Attr(Clientes)
