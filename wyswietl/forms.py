from django import forms
from .models import Odbiorca
from .models import Parametry
from .models import UOAP0
class OdbiorcaForm(forms.ModelForm):
   
    class Meta:
        model=Odbiorca
        field=('imie','nazwisko',)

class ParametryForm(forms.ModelForm):
       
     class Meta:
       model=Parametry
       field=('wysokosc','obroty','strumien',)

class UOAP0Form(forms.ModelForm):
     
     class Meta:
         model=UOAP0
         
