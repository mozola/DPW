# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wyswietl', '0010_auto_20160416_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uoap2',
            name='kat_rozwarcia_konfuzora',
            field=models.CharField(max_length=62, choices=[(0, 30), (1, 31), (2, 32), (3, 33), (4, 34), (5, 35), (6, 36), (7, 37), (8, 38), (9, 39), (10, 40), (11, 41), (12, 42), (13, 43), (14, 44), (15, 45), (16, 46), (17, 47), (18, 48), (19, 49), (20, 50), (21, 51), (22, 52), (23, 53), (24, 54), (25, 55), (26, 56), (27, 57), (28, 58), (29, 59), (30, 60), (31, 61), (32, 62), (33, 63), (34, 64), (35, 65), (36, 66), (37, 67), (38, 68), (39, 69), (40, 70), (41, 71), (42, 72), (43, 73), (44, 74), (45, 75), (46, 76), (47, 77), (48, 78), (49, 79), (50, 80), (51, 81), (52, 82), (53, 83), (54, 84), (55, 85), (56, 86), (57, 87), (58, 88), (59, 89), (60, 90)]),
            preserve_default=True,
        ),
    ]
