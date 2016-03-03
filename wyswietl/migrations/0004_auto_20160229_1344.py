# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wyswietl', '0003_auto_20160229_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametry',
            name='obroty',
            field=models.IntegerField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametry',
            name='strumien',
            field=models.IntegerField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametry',
            name='wysokosc',
            field=models.IntegerField(max_length=100),
            preserve_default=True,
        ),
    ]
