# Generated by Django 4.0.2 on 2022-02-21 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0003_contacto_gestionado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='gestionado',
            field=models.BooleanField(default=False, verbose_name='Cerrar'),
        ),
    ]