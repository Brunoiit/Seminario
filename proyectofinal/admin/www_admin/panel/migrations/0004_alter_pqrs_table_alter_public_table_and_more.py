# Generated by Django 4.2.1 on 2023-06-05 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_rename_correo_pblc_public_cuerpo_pblc_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='pqrs',
            table='PQRS',
        ),
        migrations.AlterModelTable(
            name='public',
            table='Publicaciones',
        ),
        migrations.AlterModelTable(
            name='usuarios',
            table='Usuarios',
        ),
    ]
