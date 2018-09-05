# Generated by Django 2.0.5 on 2018-08-24 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sesiones', '0003_auto_20180824_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sesion',
            name='duracion_unidad',
            field=models.CharField(blank=True, choices=[('min', 'min'), ('hr', 'hr'), ('m', 'm'), ('km', 'km')], max_length=3, verbose_name='Unidad de duración'),
        ),
    ]
