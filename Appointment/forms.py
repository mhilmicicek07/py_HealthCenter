from django import forms
from .models import *

class RandevuForm(forms.ModelForm):
    class Meta:
        model = Randevu
        fields = ('isim','email','telefon','tarih','saat','bolum','mesaj')
        label = {
            'isim':'İsim',
            'email':'Mail Adresi',
            'telefon':'Telefon Numarası',
            'tarih':'Tarih',
            'saat':'Saat',
            'bolum':'Bölüm Seçiniz',
            'mesaj':'Mesajınız',
        }

        widgets ={
            'isim': forms.TextInput(attrs={'class':'form-control','placeholder':'Adınız-Soyadınız','type':'text'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Mail Adresiniz','type':'email'}),
            'telefon': forms.NumberInput(attrs={'class':'form-control','placeholder':'Telefon Numaranız','type':'tel'}),
            'tarih': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'saat': forms.TimeInput(attrs={'class': 'form-control','type':'time'}),
            'bolum': forms.Select(attrs={'class':'form-control'}),
            'mesaj': forms.Textarea(attrs={'class':'form-control','placeholder':'Mesajınız'}),
        }