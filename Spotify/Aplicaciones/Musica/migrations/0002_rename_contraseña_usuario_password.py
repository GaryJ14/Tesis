# Generated by Django 5.0.6 on 2024-07-25 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Musica', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='password',
        ),
    ]
