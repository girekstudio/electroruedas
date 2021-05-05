# Generated by Django 3.2 on 2021-05-05 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0012_articulo_diario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articulo_diario',
            options={'verbose_name_plural': '5. Articulo Diario'},
        ),
        migrations.RemoveField(
            model_name='articulo_diario',
            name='detalle',
        ),
        migrations.AddField(
            model_name='articulo_diario',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='articulo_diario',
            name='parrafo_1',
            field=models.TextField(blank=True, max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='articulo_diario',
            name='parrafo_2',
            field=models.TextField(blank=True, max_length=800, null=True),
        ),
    ]