from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Usuarios

def index(request):
    return render(request, "index.html")

def agregar(request):
    if (request.method=="POST"):
        if (request.POST.get("name") and request.POST.get("lastname") and request.POST.get("email") and request.POST.get("phone") and request.POST.get("password")):
            user = Usuarios()
            user.nombre_usr = request.POST.get("name")
            user.apellido_usr = request.POST.get("lastname")
            user.correo_usr = request.POST.get("email")
            user.telefono_usr = request.POST.get("phone")
            user.contrasena_usr = request.POST.get("password")
            user.rol_usr = request.POST.get("rol")
            user.save()
            return redirect('ver')

    else:
        return render(request, "usuarios/agregar.html")

def eliminar(request):
    return render(request, "usuarios/eliminar.html")

def ver(request):
    return render(request, "usuarios/ver.html", {'usuarios' : Usuarios.objects.all})

def modificar(request):
    return render(request, "usuarios/modificar.html")
