# Generated by Django 4.2.7 on 2023-11-18 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogrenci', '0002_ogrenci_telefon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ogrenci',
            name='Telefon',
            field=models.IntegerField(null=True),
        ),
    ]
