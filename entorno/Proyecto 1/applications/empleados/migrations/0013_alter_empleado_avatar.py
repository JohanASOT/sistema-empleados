# Generated by Django 5.0.6 on 2024-06-27 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0012_alter_empleado_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleados', verbose_name='Imagen'),
        ),
    ]