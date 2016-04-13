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
