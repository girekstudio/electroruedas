# Generated by Django 3.2.4 on 2021-06-18 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0026_envio_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, help_text='500x800', null=True, upload_to='promo')),
            ],
            options={
                'verbose_name_plural': '8. Promo ',
            },
        ),
    ]