# Generated by Django 3.2.4 on 2021-06-18 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0030_auto_20210618_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electroruedas_galeria',
            name='imagen_distribuidor',
            field=models.ImageField(blank=True, help_text='Quieres ser distribuidor -  500*500', null=True, upload_to='electroruedas'),
        ),
    ]
