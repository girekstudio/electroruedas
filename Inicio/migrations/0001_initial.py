# Generated by Django 3.2 on 2021-04-25 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Electroruedas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favicon_amarillo', models.ImageField(help_text='imagenes 20*20', upload_to='favicon')),
                ('favicon_negro', models.ImageField(help_text='imagenes 20*20', upload_to='favicon')),
                ('logo_horizontal', models.ImageField(blank=True, help_text='imagenes 20*20', null=True, upload_to='favicon')),
                ('logo_amarillo', models.ImageField(help_text='imagenes 20*20', upload_to='favicon')),
                ('logo_negro', models.ImageField(help_text='imagenes 20*20', upload_to='favicon')),
            ],
            options={
                'verbose_name_plural': '1. Vortice',
            },
        ),
    ]
