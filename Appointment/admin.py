from django.contrib import admin
from .models import Bolum, Randevu

# Register your models here.
class RandevuAdmin(admin.ModelAdmin):
    list_display = ('isim','telefon','email','tarih','saat','bolum')

admin.site.register(Bolum)
admin.site.register(Randevu, RandevuAdmin)