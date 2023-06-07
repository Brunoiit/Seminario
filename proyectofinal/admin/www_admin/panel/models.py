from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuarios(models.Model):
    id_usr = models.IntegerField(primary_key=True,)
    nombre_usr = models.CharField(max_length=30, null=False)
    apellido_usr = models.CharField(max_length=30, null=False)
    correo_usr = models.CharField(max_length=50, null=False)
    telefono_usr = models.IntegerField(null=True)
    rol_usr = models.IntegerField(null=False)
    contrasena_usr = models.CharField(max_length=12, null=False)
    fec_creacion_usr = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'Usuarios'

class Public(models.Model):
    id_pblc = models.IntegerField(primary_key=True,)
    id_usr = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=False)
    titulo_pblc = models.CharField(max_length=25, null=False)
    cuerpo_pblc = models.CharField(max_length=500, null=False)
    fec_creacion_pblc = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'Publicaciones'

class PQRS(models.Model):
    id_pqrs = models.IntegerField(primary_key=True,)
    texto_pqrs = models.CharField(max_length=250, null=False)
    correo_pqrs = models.CharField(max_length=50, null=False)
    telefono_pqrs = models.IntegerField(null=True)
    class Meta:
        db_table = 'PQRS'

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Public, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Agregar este campo

    def __str__(self):
        return self.comentario

