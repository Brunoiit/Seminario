# Generated by Django 4.2.1 on 2023-06-04 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_pqrs_public'),
    ]

    operations = [
        migrations.RenameField(
            model_name='public',
            old_name='correo_pblc',
            new_name='cuerpo_pblc',
        ),
        migrations.RemoveField(
            model_name='public',
            name='contrasena_pblc',
        ),
        migrations.RemoveField(
            model_name='public',
            name='rol_pblc',
        ),
        migrations.RemoveField(
            model_name='public',
            name='telefono_pblc',
        ),
    ]