# Generated by Django 3.2 on 2021-04-29 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0003_auto_20210429_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='autonomia',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='motor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
