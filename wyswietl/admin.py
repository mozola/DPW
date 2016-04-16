from django.contrib import admin
from .models import Odbiorca
from .models import Parametry
from .models import UOAP0
from .models import UOAP2

class OdbiorcaAdmin(admin.ModelAdmin):
    list_display=('imie','nazwisko')
#    prepopulated_fields={'slug': ('nazwisko',)}
class ParametryAdmin(admin.ModelAdmin):
    list_display=('wysokosc','obroty','strumien')
#class ResultAdmin(admin.ModelAdmin):
    #list_display=('')

admin.site.register(Odbiorca,OdbiorcaAdmin)
admin.site.register(Parametry,ParametryAdmin)
admin.site.register(UOAP0)
admin.site.register(UOAP2)
# Register your models here.
