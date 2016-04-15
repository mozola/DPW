from django.db import models

class Odbiorca(models.Model):
     imie=models.CharField(max_length=20)
     nazwisko=models.CharField(max_length=20)
     
     def __str__(self):
         return self.nazwisko

class Parametry(models.Model):    
     wysokosc=models.IntegerField(max_length=100)
     obroty=models.IntegerField(max_length=100)
     strumien=models.IntegerField(max_length=100)

     def __str__(self):
         return self.wysokosc

class UOAP0(models.Model):
     wegiel_kamienny="Wegiel kamienny"
     wegiel_brunatny="Wegiel brunatny"
     rodzaje_paliwa=((wegiel_kamienny,'Wegiel kamienny'),(wegiel_brunatny,'Wegiel brunatny'))
     rodzaj_spalanego_paliwa=models.CharField(max_length=20,choices=rodzaje_paliwa)
     wydajnosc_kotla=models.IntegerField(max_length=20)
     masowy_udzial_wegla=models.IntegerField(max_length=10)
     masowy_udzial_wodoru=models.IntegerField(max_length=10) 
     masowy_udzial_tlenu=models.IntegerField(max_length=10)
     masowy_udzial_azotu=models.IntegerField(max_length=10)
     masowy_udzial_siarki=models.IntegerField(max_length=10)
     zawartosc_popiolu_w_paliwie_w_stanie_roboczym=models.FloatField(max_length=10)
     zawartosc_wilgoci_w_paliwie_w_stanie_roboczym=models.FloatField(max_length=10)
     wspolczynnik_nadmiaru_powietrza_w_komorze_paleniskowej=models.FloatField(max_length=10)
     udzial_popilu_unoszonego_przez_spaliny_do_kanalow_kotla=models.FloatField(max_length=5)
     srednia_zawartosc_wilgoci=models.FloatField(max_length=5)
     gestosc_CO2_w_WU=models.FloatField(max_length=5)
     gestosc_SO2_w_WU=models.FloatField(max_length=5)
     gestosc_N2_w_wu=models.FloatField(max_length=5)
     gestosc_pary_wodnej_w_WU=models.FloatField(max_length=5)
     gestosc_powietrza_w_WU=models.FloatField(max_length=5)
     przyrost_wspolczynnika_nadmiaru_powietrza_na_drodze_komora_paleniskowa_a_kanal_spalin=models.FloatField(max_length=5)
     ciesnienie_wody_zasilajacej=models.IntegerField(max_length=5)
     temperatura_wody_zasilajacej=models.IntegerField(max_length=5)
     ciesnienie_pary=models.FloatField(max_length=5)
     temperatura_pary=models.FloatField(max_length=5)
     sprawnosc_kotla=models.FloatField()
     strata_niezupelnego_spalania=models.IntegerField(max_length=5)
     podcisnienie_spalin_w_kanale=models.FloatField(max_length=5)
     temperatura_spalin_w_kanale=models.IntegerField(max_length=5)
     referencyjna_zawartosc_tlenu_w_spalinach_suchych=models.IntegerField(max_length=5)
     cisnienie_umowne=models.IntegerField(max_length=10)
     temperatura_umowna=models.IntegerField(max_length=5)


