# Generated by Django 4.0.2 on 2022-03-02 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boleta', '0005_alter_boleta_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='monto_facturado',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
