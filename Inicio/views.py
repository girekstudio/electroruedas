from django.shortcuts import render

# Create your views here.
from Clientes.models import Clientes
from Inicio.models import *
from Producto.models import *
from electroruedas.snippers import enviar_email


def index(request):
    contexto ={
        'slider': Slider.objects.all(),
        'electro_galeia': Electroruedas_galeria.objects.all().first(),
        'electro_ruedas':Marca_Electroruedas.objects.all().first(),
        'clientes': Clientes.objects.all(),
        'empresa' : Empresa.objects.all().first(),
        'beneficios': Beneficios.objects.all(),
        'ventajas': Ventajas.objects.all(),
        'articulo': Articulo_diario.objects.all().first(),
        'marcas': Marcas.objects.all(),
        'tipo_product': Tipo_producto.objects.all(),
        'product': Tipo_producto.objects.all().first(),
        'contacto_electroruedas': Contacto_electroruedas.objects.all().first(),
        'contacto_redes': Contacto_redes.objects.all().first(),

    }
    return render(request, 'index-corporate.html', contexto)

def empresa(request):
    contexto ={
        'electro_galeia': Electroruedas_galeria.objects.all().first(),
        'electro_ruedas': Marca_Electroruedas.objects.all().first(),
        'valor': Valor.objects.all(),
        'beneficios': Beneficios.objects.all(),
        'ventajas': Ventajas.objects.all(),
        'empresa': Empresa.objects.all().first(),
        'contacto_electroruedas': Contacto_electroruedas.objects.all().first(),
        'contacto_redes': Contacto_redes.objects.all().first(),

    }
    return render(request, 'about-me.html', contexto)

def productos(request):
    contexto ={
        'slider': Slider.objects.all().first(),
        'electro_ruedas':Marca_Electroruedas.objects.all().first(),
        'empresa' : Empresa.objects.all().first(),
        'marcas': Marcas.objects.all().first(),
        'tipo_product': Tipo_producto.objects.all(),
        'product': Product.objects.all(),
        'contacto_electroruedas': Contacto_electroruedas.objects.all().first(),
        'contacto_redes': Contacto_redes.objects.all().first(),
        'promo': Promo.objects.all(),
        'galeria_producto': Galeria_product.objects.all(),


    }
    return render(request, 'shop-4-columns.html', contexto)


def productos_tipo(request,id):
    contexto ={
        'electro_ruedas':Marca_Electroruedas.objects.all().first(),
        'empresa' : Empresa.objects.all().first(),
        'marcas': Marcas.objects.all().first(),
        'tipo_product': Tipo_producto.objects.filter(titulo=id),
        'product': Product.objects.filter(tipo_producto=id),
        'contacto_electroruedas': Contacto_electroruedas.objects.all().first(),
        'contacto_redes': Contacto_redes.objects.all().first(),

    }
    return render(request, 'shop-4-columns.html', contexto)


def producto(request,id):
    produc=Product.objects.all()
    prod=produc.get(id=id)
    contexto ={
        'electro_ruedas':Marca_Electroruedas.objects.all().first(),
        'empresa' : Empresa.objects.all().first(),
        'marcas': Marcas.objects.all().first(),
        'tipo_product': Tipo_producto.objects.all(),
        'product': prod,
        'productos': produc.filter(tipo_producto=prod.tipo_producto),
        'contacto_electroruedas': Contacto_electroruedas.objects.all().first(),
        'contacto_redes': Contacto_redes.objects.all().first(),
    }
    return render(request, 'shop-product-full-width.html', contexto)

def distribuidor(request):
    success=""
    if request.POST:
        nombre=request.POST.get('nombre')
        cedula = request.POST.get('cedula')
        email =request.POST.get('email')
        celular=request.POST.get('celular')
        ciudad =request.POST.get('ciudad')
        mensaje= request.POST.get('mensaje')

        mensajeFinal = "Un usuario se trata de comunicar con usted.\nNombre: %s  \nCédula:%s \nEmail: %s \ncelular: %s, de la ciudad de %s quiere comunicarse con usted y dejo el siguiente mensaje:  %s"%(
            nombre,cedula,email,celular,ciudad,mensaje
        )
        enviar_email(['electroruedas.ec@gmail.com'],'Mensaje del Sitio Web',mensajeFinal)
        success="Pronto nos comunicaremos contigo, Muchas gracias por elegir Electro Ruedas"

    contexto ={
        "mensaje":success,
        'electro_galeia': Electroruedas_galeria.objects.all().first(),
        'electro_ruedas':Marca_Electroruedas.objects.all().first(),
        'empresa' : Empresa.objects.all().first(),
        'contacto_electroruedas': Contacto_electroruedas.objects.all().first(),
        'contacto_redes': Contacto_redes.objects.all().first(),
    }
    return render(request, 'page-distribuidor.html', contexto)

def contacto(request):
    contexto ={
        'electro_ruedas':Marca_Electroruedas.objects.all().first(),
        'empresa' : Empresa.objects.all().first(),
        'contacto_electroruedas': Contacto_electroruedas.objects.all().first(),
        'contacto_redes': Contacto_redes.objects.all().first(),
    }
    return render(request, 'contact-us.html', contexto)