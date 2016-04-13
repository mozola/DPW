# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wyswietl', '0004_auto_20160229_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='UOAP0',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rodzaj_spalanego_paliwa', models.CharField(max_length=20, choices=[(b'Wegiel kamienny', b'Wegiel kamienny'), (b'Wegiel brunatny', b'Wegiel brunatny')])),
                ('wydajnosc_kotla', models.IntegerField(max_length=20)),
                ('masowy_udzial_wegla', models.IntegerField(max_length=10)),
                ('masowy_udzial_wodoru', models.IntegerField(max_length=10)),
                ('masowy_udzial_tlenu', models.IntegerField(max_length=10)),
                ('masowy_udzial_azotu', models.IntegerField(max_length=10)),
                ('masowy_udzial_siarki', models.IntegerField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
