# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wyswietl', '0009_uoap2'),
    ]

    operations = [
        migrations.AddField(
            model_name='uoap2',
            name='dlugosc_pola_elektrycznego_elektrofiltru',
            field=models.CharField(default=1, max_length=3, choices=[(3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap2',
            name='kat_rozwarcia_konfuzora',
            field=models.CharField(default=32, max_length=62, choices=[(0, 30), (1, 31), (2, 32), (3, 33), (4, 34), (5, 35), (6, 36), (7, 37), (8, 38), (9, 39), (10, 40), (11, 41), (12, 42), (13, 43), (14, 44), (15, 45), (16, 46), (17, 47), (18, 48), (19, 49), (20, 50), (21, 51), (22, 52), (23, 53), (24, 54), (25, 55), (26, 56), (27, 57), (28, 58), (29, 5930), (30, 31), (31, 32), (32, 33), (33, 34), (34, 35), (35, 36), (36, 37), (37, 38), (38, 39), (39, 40), (40, 41), (41, 42), (42, 43), (43, 44), (44, 45), (45, 46), (46, 47), (47, 48), (48, 49), (49, 50), (50, 51), (51, 52), (52, 53), (53, 54), (54, 55), (55, 56), (56, 57), (57, 58), (58, 530), (59, 31), (60, 32), (61, 33), (62, 34), (63, 35), (64, 36), (65, 37), (66, 38), (67, 39), (68, 40), (69, 41), (70, 42), (71, 43), (72, 44), (73, 45), (74, 46), (75, 47), (76, 48), (77, 49), (78, 50), (79, 51), (80, 52), (81, 53), (82, 54), (83, 55), (84, 56), (85, 57), (86, 58), (87, 59), (88, 60), (89, 6), (90, 600)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap2',
            name='predkosc_spalin_w_komorze_elektrofiltru',
            field=models.FloatField(default=1.0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap2',
            name='wysokosc_pola_elektrycznego_elektrofiltru',
            field=models.FloatField(default=123, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uoap2',
            name='predkosc_spalin_w_kanale',
            field=models.CharField(max_length=6, choices=[(15, b'15'), (16, b'16'), (17, b'17'), (18, b'18'), (19, b'19'), (20, b'20')]),
            preserve_default=True,
        ),
    ]
