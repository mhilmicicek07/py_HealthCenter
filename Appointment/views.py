from django.shortcuts import render, redirect
from .models import Randevu
from .forms import RandevuForm
from django.contrib import messages
from News.models import News
from Payment.views import *

def randevu_view(request):
    news = News.objects.all()
    if request.method == 'POST':
        form = RandevuForm(request.POST)
        if form.is_valid():
            tarih = form.cleaned_data.get('tarih')
            saat = form.cleaned_data.get('saat')
            bolum = form.cleaned_data.get('bolum')

            if Randevu.objects.filter(tarih=tarih, saat=saat, bolum=bolum).exists():
                messages.error(request, 'Lütfen farklı bir tarih/saat seçiniz!')
            else:
                form.save()
                messages.success(request, 'Randevu kayıt işlemi başarılı!')
                return redirect('/payment/')
        # else:
        #     form = RandevuForm()

        return render(request, 'Appointment/appointment.html', {
            'form': form,
            'news': news,
        })
    else:
        form = RandevuForm()

    return render(request, 'Appointment/appointment.html', {
        'form': form,
        'news': news,
    })
#! #TODO: mesajlar sayfada görünmüyor sebebini çözemedim.