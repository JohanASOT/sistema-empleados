# Generated by Django 5.0.6 on 2024-06-17 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='cantidad',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='subtitle',
            field=models.CharField(max_length=50, verbose_name='Subtitulo'),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Titulo'),
        ),
    ]
