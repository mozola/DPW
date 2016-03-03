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
 
