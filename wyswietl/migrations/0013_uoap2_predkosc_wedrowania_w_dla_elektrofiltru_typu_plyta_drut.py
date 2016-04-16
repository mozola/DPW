# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wyswietl', '0012_auto_20160416_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='uoap2',
            name='predkosc_wedrowania_w_dla_elektrofiltru_typu_plyta_drut',
            field=models.FloatField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
