# Generated by Django 4.0.2 on 2022-02-25 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boleta', '0003_alter_boleta_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='comentario',
            field=models.TextField(verbose_name='¿Cuéntanos cómo lo estás haciendo?'),
        ),
        migrations.AlterField(
            model_name='boleta',
            name='fecha_emision',
            field=models.DateField(verbose_name='Fecha de emisión boleta'),
        ),
        migrations.AlterField(
            model_name='boleta',
            name='mts3',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='m3 facturados (consumo del mes)'),
        ),
        migrations.AlterField(
            model_name='boleta',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='boleta/uploads/', verbose_name='Ingresar boleta (formato pdf, jpg o png)'),
        ),
    ]