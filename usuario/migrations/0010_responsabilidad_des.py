# Generated by Django 4.0.2 on 2022-02-22 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0009_voluntario_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsabilidad',
            name='des',
            field=models.TextField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
