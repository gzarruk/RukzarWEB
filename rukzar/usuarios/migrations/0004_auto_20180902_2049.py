# Generated by Django 2.0.5 on 2018-09-02 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20180902_2017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfilusuario',
            old_name='usuario',
            new_name='user',
        ),
    ]
