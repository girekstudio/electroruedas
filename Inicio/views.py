from django.shortcuts import render

# Create your views here.
from Inicio.models import *


def index(request):
    contexto ={
        'electroruedas':Electroruedas.objects.all().first(),
    }
    return render(request, 'index-corporate.html', contexto)

def empresa(request):
    contexto ={
        'electroruedas':Electroruedas.objects.all().first(),
    }
    return render(request, 'about-me.html', contexto)

def productos(request):
    contexto ={
        'electroruedas':Electroruedas.objects.all().first(),
    }
    return render(request, 'shop-4-columns.html', contexto)

def producto(request):
    contexto ={
        'electroruedas':Electroruedas.objects.all().first(),
    }
    return render(request, 'shop-product-full-width.html', contexto)

def distribuidor(request):
    contexto ={
        'electroruedas':Electroruedas.objects.all().first(),
    }
    return render(request, 'page-distribuidor.html', contexto)

def contacto(request):
    contexto ={
        'electroruedas':Electroruedas.objects.all().first(),
    }
    return render(request, 'contact-us.html', contexto)