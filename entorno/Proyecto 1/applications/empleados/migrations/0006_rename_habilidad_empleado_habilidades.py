# Generated by Django 5.0.6 on 2024-06-12 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0005_rename_habilidades_empleado_habilidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='habilidad',
            new_name='habilidades',
        ),
    ]