# Generated by Django 2.1.3 on 2018-11-10 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Escuela', '0002_profesor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='nombres',
            new_name='nombre',
        ),
    ]