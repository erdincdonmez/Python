# Generated by Django 4.2.7 on 2023-11-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogrenci', '0004_veli'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ogretmen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TC', models.CharField(max_length=11)),
                ('AdiSoyadi', models.CharField(max_length=50)),
                ('Bransi', models.CharField(max_length=30)),
            ],
        ),
    ]
