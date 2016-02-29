from django import forms
from .models import Odbiorca
from .models import Parametry

class OdbiorcaForm(forms.ModelForm):
   
    class Meta:
        model=Odbiorca
        field=('imie','nazwisko',)

class ParametryForm(forms.ModelForm):
       
     class Meta:
       model=Parametry
       field=('wysokosc','obroty','strumien',)
