# Generated by Django 5.1.6 on 2025-02-07 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trabajadores', '0002_rename_modalidad_personas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personas',
            old_name='modalidad',
            new_name='personas',
        ),
    ]
