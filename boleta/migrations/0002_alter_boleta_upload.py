# Generated by Django 4.0.2 on 2022-02-25 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boleta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='upload',
            field=models.FileField(upload_to='boleta/uploads/'),
        ),
    ]
