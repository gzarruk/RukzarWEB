# Generated by Django 2.0.5 on 2018-08-28 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sesiones', '0007_auto_20180826_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='sesion',
            name='periodo',
            field=models.CharField(blank=True, choices=[('BA', 'Base'), ('PR', 'Progresión'), ('CE', 'Cenít'), ('CO', 'Competencia')], max_length=10),
        ),
        migrations.AlterField(
            model_name='sesion',
            name='comentarios',
            field=models.TextField(blank=True, max_length=5000, verbose_name='Comentarios'),
        ),
        migrations.AlterField(
            model_name='sesion',
            name='descripcion',
            field=models.TextField(max_length=5000, verbose_name='Descripción'),
        ),
    ]
