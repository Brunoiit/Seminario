# Generated by Django 4.2.1 on 2023-06-08 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0011_calculo_remove_usuarios_usuario_dato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='id_usr',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
