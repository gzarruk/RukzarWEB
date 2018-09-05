# Generated by Django 2.0.5 on 2018-08-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sesiones', '0002_auto_20180824_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sesion',
            name='actividad',
            field=models.CharField(choices=[('NT', 'Natación'), ('CL', 'Ciclismo'), ('AT', 'Atletismo'), ('FZ', 'Fuerza'), ('DS', 'Descanso'), ('CD', 'Otra-Cardio')], max_length=264, unique=True),
        ),
    ]