from django.shortcuts import render

# Create your views here.
from Clientes.models import Clientes
from Inicio.models import *
from Producto.models import *


def index(request):
    contexto ={
        'slider': Slider.objects.all(),
        'electro_galeia': Electroruedas_galeria.objects.all().first(),
        'electro_ruedas':Electroruedas.objects.all().first(),
        'clientes': Clientes.objects.all(),
        'empresa' : Empresa.objects.all().first(),
        'beneficios': Beneficios.objects.all(),
        'marcas': Marcas.objects.all(),
        'tipo_product': Tipo_producto.objects.all().first(),
        'product': Tipo_producto.objects.all().first(),
        'contacto_electroruedas': Contacto_electroruedas.objects.all().first(),
        'contacto_redes': Contacto_redes.objects.all().first(),

    }
    return render(request, 'index-corporate.html', contexto)

def empresa(request):
    contexto ={
        'electro_galeia': Electroruedas_galeria.objects.all().first(),
        'electro_ruedas': Electroruedas.objects.all().first(),
        'valor': Valor.objects.all(),
        'empresa': Empresa.objects.all().first(),
    }
    return render(request, 'about-me.html', contexto)

def productos(request):
    contexto ={
        'slider': Slider.objects.all().first(),
        'electro_ruedas':Electroruedas.objects.all().first(),
        'empresa' : Empresa.objects.all().first(),
        'marcas': Marcas.objects.all().first(),
        'tipo_product': Tipo_producto.objects.all(),
        'product': Product.objects.all(),
        'contacto_electroruedas': Contacto_electroruedas.objects.all().first(),
        'contacto_redes': Contacto_redes.objects.all().first(),

    }
    return render(request, 'shop-4-columns.html', contexto)

def producto(request,id):
    contexto ={
        'electro_ruedas':Electroruedas.objects.all().first(),
        'empresa' : Empresa.objects.all().first(),
        'marcas': Marcas.objects.all().first(),
        'tipo_product': Tipo_producto.objects.all(),
        'product': Product.objects.get(id=id),
        'productos': Product.objects.all(),
        'contacto_electroruedas': Contacto_electroruedas.objects.all().first(),
        'contacto_redes': Contacto_redes.objects.all().first(),
    }
    return render(request, 'shop-product-full-width.html', contexto)

def distribuidor(request):
    contexto ={
        'electro_ruedas':Electroruedas.objects.all().first(),
        'empresa' : Empresa.objects.all().first(),
    }
    return render(request, 'page-distribuidor.html', contexto)

def contacto(request):
    contexto ={
        'electro_ruedas':Electroruedas.objects.all().first(),
        'empresa' : Empresa.objects.all().first(),
        'contacto_electroruedas': Contacto_electroruedas.objects.all().first(),
        'contacto_redes': Contacto_redes.objects.all().first(),
    }
    return render(request, 'contact-us.html', contexto)