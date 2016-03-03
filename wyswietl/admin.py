from django.contrib import admin
from .models import Odbiorca
from .models import Parametry

class OdbiorcaAdmin(admin.ModelAdmin):
    list_display=('imie','nazwisko')
#    prepopulated_fields={'slug': ('nazwisko',)}
class ParametryAdmin(admin.ModelAdmin):
    list_display=('wysokosc','obroty','strumien')
#class ResultAdmin(admin.ModelAdmin):
    #list_display=('')

admin.site.register(Odbiorca,OdbiorcaAdmin)
admin.site.register(Parametry,ParametryAdmin)
#admin.site.register(Result,ResultAdmin)

# Register your models here.
