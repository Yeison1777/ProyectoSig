# Generated by Django 5.2 on 2025-06-20 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('color', '0001_initial'),
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenProductoColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='productos/color/')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='color.color')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_color', to='producto.producto')),
            ],
            options={
                'db_table': 'imagen_producto_color',
            },
        ),
    ]
