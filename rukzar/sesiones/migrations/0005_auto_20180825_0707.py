# Generated by Django 2.0.5 on 2018-08-25 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sesiones', '0004_auto_20180824_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sesion',
            name='nombre',
            field=models.CharField(max_length=264),
        ),
    ]
