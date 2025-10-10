from django import forms
from .models import *
from datetime import time, timedelta, datetime

class RandevuForm(forms.ModelForm):
    class Meta:
        model = Randevu
        fields = ('isim', 'email', 'telefon', 'tarih', 'saat', 'bolum', 'mesaj')
        labels = {
            'isim': 'İsim',
            'email': 'Mail Adresi',
            'telefon': 'Telefon Numarası',
            'tarih': 'Tarih',
            'saat': 'Saat',
            'bolum': 'Bölüm Seçiniz',
            'mesaj': 'Mesajınız',
        }

        widgets = {
            'isim': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız-Soyadınız', 'type': 'text'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Mail Adresiniz', 'type': 'email'}),
            'telefon': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Telefon Numaranız', 'type': 'tel'}),
            'tarih': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'bolum': forms.Select(attrs={'class': 'form-control'}),
            'mesaj': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mesajınız'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Saat seçenekleri oluşturuluyor
        self.fields['saat'] = forms.ChoiceField(
            choices=self.generate_time_choices(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            label='Saat'
        )

    def generate_time_choices(self):
        """09:00–12:00 ve 13:00–17:00 arasında 45 dk seans + 15 dk ara"""
        choices = []
        sabah_basla = datetime.strptime("09:00", "%H:%M")
        sabah_bitis = datetime.strptime("12:00", "%H:%M")
        ogle_basla = datetime.strptime("13:00", "%H:%M")
        ogle_bitis = datetime.strptime("17:00", "%H:%M")

        def zaman_araligi(baslangic, bitis):
            zaman = baslangic
            while zaman < bitis:
                son = zaman + timedelta(minutes=45)
                if son <= bitis:
                    choices.append((zaman.strftime("%H:%M"), zaman.strftime("%H:%M")))
                zaman += timedelta(minutes=60)  # 45 dk seans + 15 dk ara

        zaman_araligi(sabah_basla, sabah_bitis)
        zaman_araligi(ogle_basla, ogle_bitis)

        return choices