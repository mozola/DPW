# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wyswietl', '0008_auto_20160415_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='UOAP2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('predkosc_spalin_w_kanale', models.CharField(max_length=3, choices=[(15, b'15'), (16, b'16'), (17, b'17'), (18, b'18')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
