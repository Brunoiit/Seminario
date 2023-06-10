from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render, redirect
from .models import Usuarios, Public, PQRS, Comentario, Calculo, Dato
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from . import views

@login_required
def agregar(request):
    if request.user.is_authenticated:
        if (request.method=="POST"):
            if (request.POST.get("name") and request.POST.get("lastname") and request.POST.get("email") and request.POST.get("phone") and request.POST.get("password")):
                usuario = Usuarios()
                usuario.nombre_usr = request.POST.get("name")
                usuario.apellido_usr = request.POST.get("lastname")
                usuario.correo_usr = request.POST.get("email")
                usuario.telefono_usr = request.POST.get("phone")
                usuario.contrasena_usr = request.POST.get("password")
                usuario.rol_usr = request.POST.get("rol")
                usuario.save()
                primeras_letras_apellido = request.POST.get("lastname")[:2]

                # Crear el nombre de usuario combinando el nombre y las primeras letras del apellido
                nombre_usuario = f"{request.POST.get('name')}{primeras_letras_apellido}"
                user = User.objects.create_user(username=nombre_usuario, first_name= request.POST.get("name"), last_name = request.POST.get("lastname"),email=request.POST.get("email"), password=request.POST.get("password"))
                return redirect('ver')
            return HttpResponse("Usuario autenticado")
        else:
            return render(request, "usuarios/agregar.html")
    else:
        # En caso de que el usuario no esté autenticado
        return HttpResponse("Usuario no autenticado")
    
def index(request):
    publicaciones = Public.objects.order_by('-fec_creacion_pblc')
    datos_publicaciones = []
    for publicacion in publicaciones:
        usuario = Usuarios.objects.get(id_usr=publicacion.id_usr_id)  # Acceder a id_usr_id en lugar de id_usr
        datos_publicaciones.append({
            'publicacion': publicacion,
            'usuario': usuario,
        })
    return render(request, 'index.html', {'datos_publicaciones': datos_publicaciones})


def cerrarSesion(request):
    logout(request)
    return redirect("/")

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                return redirect('ver')
        except User.DoesNotExist:
            pass
        return render(request, 'login.html', {'error_message': 'Credenciales inválidas'})
    else:
        return render(request, 'login.html')

# @login_required
# def eliminar(request, id_usr):
#     usuario = get_object_or_404(Usuarios, id_usr=id_usr)    
#     if request.method == "POST":
#         # Desactivar el usuario en la tabla de usuarios de Django
#         django_user = User.objects.get(email=usuario.correo_usr)
#         django_user.is_active = False
#         django_user.save()        
#         # Eliminar el usuario de la tabla Usuarios
#         usuario.delete()        
#         return redirect('ver')    
#     return render(request, "usuarios/eliminar.html", {'usuario': usuario})

@login_required
def ver(request):
    usuario_actual = request.user.id  # Obtener el usuario autenticado
    try:
        usuario = Usuarios.objects.get(id_usr=usuario_actual)  # Obtener el objeto Usuarios correspondiente
        mostrar_boton = usuario.rol_usr == 1  # Verificar el rol del usuario
    except Usuarios.DoesNotExist:
        mostrar_boton = False

    usuarios = Usuarios.objects.all()

    return render(request, "usuarios/ver.html", {'usuarios': usuarios, 'mostrar_boton': mostrar_boton})

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

@login_required
def publicar(request):
    if request.method == "POST":
        if request.POST.get("tittle") and request.POST.get("cuerpo"):
            publicacion = Public()
            usuario = Usuarios.objects.get(id_usr=request.user.id)
            publicacion.id_usr_id = usuario.id_usr
            publicacion.titulo_pblc = request.POST.get("tittle")
            publicacion.cuerpo_pblc = request.POST.get("cuerpo")
            publicacion.save()
            return redirect('/')
    return render(request, "publicaciones/publicar.html")

def detalle_publicacion(request, id_pblc):
    publicacion = get_object_or_404(Public, id_pblc=id_pblc)
    comentarios = Comentario.objects.filter(publicacion=publicacion).order_by('-fecha_creacion')  # Obtener los comentarios de la publicación ordenados por fecha de creación descendente
    context = {
        'publicacion': publicacion,
        'comentarios': comentarios,  # Agregar los comentarios al contexto
    }
    return render(request, "publicaciones/detalle_publicacion.html", context)



@login_required
def guardar_comentario(request):
    if request.method == 'POST':
        comentario_texto = request.POST.get('comentario')
        publicacion_id = request.POST.get('publicacion_id')
        usuario = get_object_or_404(Usuarios, id_usr=request.user.id)
        publicacion = get_object_or_404(Public, id_pblc=publicacion_id)
        comentario = Comentario(usuario=usuario, publicacion=publicacion, comentario=comentario_texto)
        comentario.save()
    return redirect(request.META['HTTP_REFERER'])

def agregar_datos(request, calculo_id):
    calculo = Calculo.objects.get(id_calculo=calculo_id)

    if request.method == 'POST':
        objeto = request.POST['objeto']
        consumo_wh = request.POST['consumo_wh']
        promedio_horas_diarias = request.POST['promedio_horas_diarias']

        Dato.objects.create(calculo=calculo, objeto=objeto, consumo_wh=consumo_wh, promedio_horas_diarias=promedio_horas_diarias)
        
        return redirect('procesar_calculo', calculo_id=calculo_id)

    return render(request, 'agregar_datos.html', {'calculo': calculo})

