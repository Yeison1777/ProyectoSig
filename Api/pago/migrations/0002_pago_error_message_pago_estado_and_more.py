# Generated by Django 5.2 on 2025-07-12 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pago', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='error_message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pago',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('proceso', 'En Proceso'), ('realizado', 'Realizado'), ('fallido', 'Fallido'), ('cancelado', 'Cancelado'), ('requires_payment_method', 'Requiere Método de Pago'), ('requires_confirmation', 'Requiere Confirmación'), ('requires_action', 'Requiere Acción'), ('processing', 'Procesando'), ('succeeded', 'Exitoso'), ('canceled', 'Cancelado')], default='pendiente', max_length=30),
        ),
        migrations.AddField(
            model_name='pago',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='pago',
            name='observaciones',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pago',
            name='stripe_charge_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pago',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pago',
            name='stripe_payment_intent_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pago',
            name='stripe_payment_method_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pago',
            name='metodo_pago',
            field=models.CharField(choices=[('qr', 'QR'), ('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta'), ('stripe', 'Stripe')], max_length=10),
        ),
    ]
