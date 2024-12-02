# Generated by Django 5.1 on 2024-11-22 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('id_sucursal', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre_suc', models.CharField(max_length=100)),
                ('direccion_suc', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=100)),
                ('telefono_suc', models.CharField(max_length=20)),
                ('id_proveedor', models.IntegerField()),
            ],
        ),
    ]