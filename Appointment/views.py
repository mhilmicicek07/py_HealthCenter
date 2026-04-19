from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Randevu
from .forms import RandevuForm
from News.models import News

def randevu_view(request):
    news = News.objects.all()
    form = RandevuForm(request.POST or None)

    if request.method == 'POST':
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
        else:
            messages.error(request, 'Lütfen formu kontrol ediniz.')

    return render(request, 'Appointment/appointment.html', {
        'form': form,
        'news': news,
    })
#! #TODO: mesajlar sayfada görünmüyor sebebini çözemedim.
