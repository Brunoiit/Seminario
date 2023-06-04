from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id_usr = models.IntegerField(primary_key=True,)
    nombre_usr = models.CharField(max_length=30, null=False)
    apellido_usr = models.CharField(max_length=30, null=False)
    correo_usr = models.CharField(max_length=50, null=False)
    telefono_usr = models.IntegerField(null=True)
    rol_usr = models.IntegerField(null=False)
    fec_creacion_usr = models.DateTimeField(auto_now_add=True, null=True)
    class meta:
        db_table = 'Usuarios'