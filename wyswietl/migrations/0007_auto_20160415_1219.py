# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wyswietl', '0006_auto_20160415_0712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uoap0',
            old_name='ciesnienie_pary',
            new_name='cisnienie_pary',
        ),
        migrations.RenameField(
            model_name='uoap0',
            old_name='ciesnienie_wody_zasilajacej',
            new_name='cisnienie_wody_zasilajacej',
        ),
        migrations.RenameField(
            model_name='uoap0',
            old_name='gestosc_N2_w_wu',
            new_name='gestosc_N2_w_Wu',
        ),
        migrations.RenameField(
            model_name='uoap0',
            old_name='udzial_popilu_unoszonego_przez_spaliny_do_kanalow_kotla',
            new_name='udzial_popiolu_unoszonego_przez_spaliny_do_kanalow_kotla',
        ),
    ]
