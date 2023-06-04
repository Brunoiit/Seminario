from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render, redirect
from .models import Usuarios
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect
from . import views

def index(request):
    return render(request, "index.html")

def cerrarSesion(request):
    logout(request)
    return redirect("/")

@login_required
def agregar(request):
    if request.user.is_authenticated:
        # Tu lógica aquí
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
            return HttpResponse("Usuario autenticado")
        else:
            return render(request, "usuarios/agregar.html")
    else:
        # En caso de que el usuario no esté autenticado
        return HttpResponse("Usuario no autenticado")
    

@login_required
def eliminar(request, id_usr):
    usuario = get_object_or_404(Usuarios, id_usr=id_usr)
    
    if request.method == "POST":
        usuario.delete()
        return redirect('ver')
    
    return render(request, "usuarios/eliminar.html", {'usuario': usuario})

@login_required
def ver(request):
    return render(request, "usuarios/ver.html", {'usuarios' : Usuarios.objects.all})

@login_required
def modificar(request, id_usr):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST.get("name") and request.POST.get("lastname") and request.POST.get("email") and request.POST.get("phone") and request.POST.get("password"):
                user = Usuarios.objects.get(id_usr=id_usr)
                user.nombre_usr = request.POST.get("name")
                user.apellido_usr = request.POST.get("lastname")
                user.correo_usr = request.POST.get("email")
                user.telefono_usr = request.POST.get("phone")
                user.contrasena_usr = request.POST.get("password")
                user.rol_usr = request.POST.get("rol")
                user.save()
                return redirect("ver")
            return HttpResponse("Usuario autenticado")
        else:
            usuario = Usuarios.objects.get(id_usr=id_usr)
            return render(request, "usuarios/modificar.html", {'usuario': usuario})
    else:
        # En caso de que el usuario no esté autenticado
        return HttpResponse("Usuario no autenticado")


