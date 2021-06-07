# Generated by Django 3.2 on 2021-06-05 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0022_beneficios_ventajas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='sub_titulo_1',
            new_name='sub_titulo_marcas',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='titulo_1',
            new_name='titulo_marcas',
        ),
        migrations.AddField(
            model_name='empresa',
            name='titulo_ventajas',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
