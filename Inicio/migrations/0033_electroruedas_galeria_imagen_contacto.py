# Generated by Django 3.2.4 on 2021-06-18 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0032_auto_20210618_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='electroruedas_galeria',
            name='imagen_contacto',
            field=models.ImageField(blank=True, help_text='Quieres ser distribuidor -  500*900', null=True, upload_to='electroruedas'),
        ),
    ]