# Generated by Django 5.2 on 2025-06-27 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario',
            name='descripcion_producto',
        ),
        migrations.AddField(
            model_name='inventario',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='producto.producto'),
        ),
    ]
