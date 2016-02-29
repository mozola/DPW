# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wyswietl', '0002_auto_20160223_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wysokosc', models.CharField(max_length=100)),
                ('obroty', models.CharField(max_length=100)),
                ('strumien', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='odbiorca',
            name='obroty',
        ),
        migrations.RemoveField(
            model_name='odbiorca',
            name='strumien',
        ),
        migrations.RemoveField(
            model_name='odbiorca',
            name='wysokosc',
        ),
    ]
