# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-18 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=8, verbose_name='Latitude')),
                ('lng', models.DecimalField(decimal_places=6, max_digits=8, verbose_name='Longitude')),
            ],
        ),
        migrations.AlterField(
            model_name='greeting',
            name='when',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]