# Generated by Django 4.2.1 on 2023-06-10 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0012_alter_usuarios_id_usr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dato',
            name='calculo',
        ),
        migrations.DeleteModel(
            name='Calculo',
        ),
        migrations.DeleteModel(
            name='Dato',
        ),
    ]
