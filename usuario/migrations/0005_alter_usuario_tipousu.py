# Generated by Django 4.0.2 on 2022-02-19 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_usuario_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipousu',
            field=models.CharField(max_length=100, verbose_name='Tipo de Usuario'),
        ),
    ]
