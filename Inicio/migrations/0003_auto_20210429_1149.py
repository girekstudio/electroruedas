# Generated by Django 3.2 on 2021-04-29 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0002_auto_20210428_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto_electroruedas',
            name='horario_dom',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacto_electroruedas',
            name='horario_lu_vier',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacto_electroruedas',
            name='horario_sab',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
