# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wyswietl', '0005_uoap0'),
    ]

    operations = [
        migrations.AddField(
            model_name='uoap0',
            name='ciesnienie_pary',
            field=models.FloatField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='ciesnienie_wody_zasilajacej',
            field=models.IntegerField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='cisnienie_umowne',
            field=models.IntegerField(default='1', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='gestosc_CO2_w_WU',
            field=models.FloatField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='gestosc_N2_w_wu',
            field=models.FloatField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='gestosc_SO2_w_WU',
            field=models.FloatField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='gestosc_pary_wodnej_w_WU',
            field=models.FloatField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='gestosc_powietrza_w_WU',
            field=models.FloatField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='podcisnienie_spalin_w_kanale',
            field=models.FloatField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='przyrost_wspolczynnika_nadmiaru_powietrza_na_drodze_komora_paleniskowa_a_kanal_spalin',
            field=models.FloatField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='referencyjna_zawartosc_tlenu_w_spalinach_suchych',
            field=models.IntegerField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='sprawnosc_kotla',
            field=models.FloatField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='srednia_zawartosc_wilgoci',
            field=models.FloatField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='strata_niezupelnego_spalania',
            field=models.IntegerField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='temperatura_pary',
            field=models.FloatField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='temperatura_spalin_w_kanale',
            field=models.IntegerField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='temperatura_umowna',
            field=models.IntegerField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='temperatura_wody_zasilajacej',
            field=models.IntegerField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='udzial_popilu_unoszonego_przez_spaliny_do_kanalow_kotla',
            field=models.FloatField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='wspolczynnik_nadmiaru_powietrza_w_komorze_paleniskowej',
            field=models.FloatField(default='1', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='zawartosc_popiolu_w_paliwie_w_stanie_roboczym',
            field=models.FloatField(default='1', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uoap0',
            name='zawartosc_wilgoci_w_paliwie_w_stanie_roboczym',
            field=models.FloatField(default='1', max_length=10),
            preserve_default=False,
        ),
    ]
