# Generated by Django 5.2 on 2025-07-12 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nota_venta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notaventa',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('procesando', 'Procesando'), ('pagada', 'Pagada'), ('cancelada', 'Cancelada')], max_length=20),
        ),
    ]
