from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Familiar

# Create your views here.

def saludar(request):
    return HttpResponse("BIENVENIDO COMO ESTAN TODOS")

def despedida(request):
    return HttpResponse("ADIOS A TODOS")

def saludo_nombre(request, nombre):
    return HttpResponse(f"HOLA COMO ESTAS {nombre}")

def despedida_nombre(request, nombre):
    return HttpResponse(f"HASTA LUEGO {nombre}")

def primer_template(request):
    return render(request, 'AppCoder/index.html')

def segundo_template(request, nombres, apellidos, carrera):
    return render(request, 'AppCoder/index2.html',
    {
        "nombres" : nombres,
        "apellidos" : apellidos,
        "carrera" : carrera
    })

def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "AppCoder/familiares.html", 
    {
    "lista_familiares": lista_familiares
    })