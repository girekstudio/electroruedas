# Generated by Django 3.2 on 2021-06-05 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0020_rename_beneficioss_beneficios'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Beneficios',
        ),
        migrations.DeleteModel(
            name='Ventajas',
        ),
    ]