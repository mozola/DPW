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
     udzial_popiolu_unoszonego_przez_spaliny_do_kanalow_kotla=models.FloatField(max_length=5)
     srednia_zawartosc_wilgoci=models.FloatField(max_length=5)
     gestosc_CO2_w_WU=models.FloatField(max_length=5)
     gestosc_SO2_w_WU=models.FloatField(max_length=5)
     gestosc_N2_w_WU=models.FloatField(max_length=5)
     gestosc_pary_wodnej_w_WU=models.FloatField(max_length=5)
     gestosc_powietrza_w_WU=models.FloatField(max_length=5)
     przyrost_wspolczynnika_nadmiaru_powietrza_na_drodze_komora_paleniskowa_a_kanal_spalin=models.FloatField(max_length=5)
     cisnienie_wody_zasilajacej=models.IntegerField(max_length=5)
     temperatura_wody_zasilajacej=models.IntegerField(max_length=5)
     cisnienie_pary=models.FloatField(max_length=5)
     temperatura_pary=models.FloatField(max_length=5)
     sprawnosc_kotla=models.FloatField()
     strata_niezupelnego_spalania=models.IntegerField(max_length=5)
     podcisnienie_spalin_w_kanale=models.FloatField(max_length=5)
     temperatura_spalin_w_kanale=models.IntegerField(max_length=5)
     referencyjna_zawartosc_tlenu_w_spalinach_suchych=models.IntegerField(max_length=5)
     cisnienie_umowne=models.IntegerField(max_length=10)
     temperatura_umowna=models.IntegerField(max_length=5)

class UOAP2(models.Model):
     predkosci=((15,'15'),(16,'16'),(17,'17'),(18,'18'),(19,'19'),(20,'20'))
     predkosc_spalin_w_kanale=models.CharField(max_length=6,choices=predkosci)
     dlugosci=((3,'3'),(4,'4'),(5,'5'))
     dlugosc_pola_elektrycznego_elektrofiltru=models.CharField(max_length=3,choices=dlugosci)
     wysokosc_pola_elektrycznego_elektrofiltru=models.FloatField(max_length=5)
     predkosc_spalin_w_komorze_elektrofiltru=models.FloatField(max_length=5)
     kat=enumerate((30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90))    
     kat_rozwarcia_konfuzora=models.CharField(max_length=62,choices=kat)
     kat2=enumerate((45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60))
     kat_pochylenia_sciany_leja_do_poziomu=models.CharField(max_length=26,choices=kat2)
     kat3=enumerate((90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120))
     kat_rozwarcia_konfuzora=models.CharField(max_length=31,choices=kat3)
     wymiar=enumerate((200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500))
     wymiary_bokow_otworu_wylotowego_leja_o_ksztalcie_prostokatnym=models.CharField(max_length=300, choices=wymiar)
     predkosc_wedrowania_w_dla_elektrofiltru_typu_plyta_drut=models.FloatField(max_length=10)

