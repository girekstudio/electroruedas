# Generated by Django 3.2 on 2021-04-29 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0010_electroruedas_galeria_imagen_6'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='sub_titulo_5',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='sub_titulo_6',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='titulo_5',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='titulo_6',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
