# Generated by Django 2.0.5 on 2018-09-02 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20180902_2049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfilusuario',
            old_name='user',
            new_name='usuario',
        ),
    ]