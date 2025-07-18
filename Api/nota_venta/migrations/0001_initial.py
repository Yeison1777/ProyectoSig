# Generated by Django 5.2 on 2025-07-10 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotaVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('pagada', 'Pagada'), ('cancelada', 'Cancelada')], max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas_venta', to='cliente.cliente')),
            ],
            options={
                'db_table': 'nota_venta',
                'permissions': [('crear_nota_venta', 'Puede crear nota de venta'), ('editar_nota_venta', 'Puede editar nota de venta'), ('eliminar_nota_venta', 'Puede eliminar nota de venta'), ('ver_nota_venta', 'Puede ver nota de venta')],
                'default_permissions': (),
            },
        ),
    ]
