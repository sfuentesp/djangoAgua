# Generated by Django 4.0.2 on 2022-02-26 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boleta', '0004_alter_boleta_comentario_alter_boleta_fecha_emision_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Ingresar boleta (formato pdf, jpg o png)'),
        ),
    ]
