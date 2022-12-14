# Generated by Django 4.1 on 2022-09-23 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='titre')),
                ('url_img', models.CharField(max_length=42, verbose_name='url_img')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 23, 10, 4, 22, 339347))),
                ('code', models.CharField(max_length=30, null=True, verbose_name='code')),
                ('keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='mots clé')),
                ('for_sale', models.BooleanField()),
                ('categorie', models.CharField(max_length=42, verbose_name='titre')),
                ('caracteristic', models.CharField(max_length=255, verbose_name='caractéristiques')),
            ],
        ),
    ]
