from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def agregar(request):
    return render(request, "usuarios/agregar.html")

def eliminar(request):
    return render(request, "usuarios/eliminar.html")

def ver(request):
    return render(request, "usuarios/ver.html")

def modificar(request):
    return render(request, "usuarios/modificar.html")
