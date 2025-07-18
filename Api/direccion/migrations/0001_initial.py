# Generated by Django 5.2 on 2025-07-10 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=100)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
            options={
                'db_table': 'direccion',
                'permissions': [('crear_direccion', 'Puede crear dirección'), ('editar_direccion', 'Puede editar dirección'), ('eliminar_direccion', 'Puede eliminar dirección'), ('ver_direccion', 'Puede ver dirección')],
                'default_permissions': (),
            },
        ),
    ]
