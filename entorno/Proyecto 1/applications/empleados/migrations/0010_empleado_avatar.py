# Generated by Django 5.0.6 on 2024-06-27 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0009_alter_empleado_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(default=True, upload_to='empleados', verbose_name='Imagen'),
        ),
    ]
