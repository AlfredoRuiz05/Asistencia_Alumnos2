# Generated by Django 5.0.4 on 2024-06-05 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_biografia'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='es_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='es_alumno',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='es_profesor',
            field=models.BooleanField(default=False),
        ),
    ]