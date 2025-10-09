from django.shortcuts import render, redirect
import iyzipay
import json
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from Appointment.forms import RandevuForm

api_key = 'sandbox-4pXMNqLNKKyHdjhPdsAOpgsJt3wlOSqU'
secret_key = 'sandbox-z9a7giJpDFJBemWw5l6HZVEPGvbGa9lk'
base_url = 'sandbox-api.iyzipay.com'

options = {
    'api_key': api_key,
    'secret_key': secret_key,
    'base_url': base_url,
}


@csrf_exempt
def payment(request):
    buyer = {
        'id': 'BY789',
        'name': 'John',
        'surname': 'Doe',
        'gsmNumber': '+905350000000',
        'email': 'email@email.com',
        'identityNumber': '74300864791',
        'lastLoginDate': '2015-10-05 12:43:35',
        'registrationDate': '2013-04-21 15:12:09',
        'registrationAddress': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'ip': '85.34.78.112',
        'city': 'Istanbul',
        'country': 'Turkey',
        'zipCode': '34732'
    }

    address = {
        'contactName': 'Jane Doe',
        'city': 'Istanbul',
        'country': 'Turkey',
        'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'zipCode': '34732'
    }

    basket_items = [
        {'id': 'BI101', 'name': 'Randevu Ücreti', 'category1': 'Sağlık', 'itemType': 'VIRTUAL', 'price': '500.0'},
    ]

    iyzico_request = {
        'locale': 'tr',
        'conversationId': '123456789',
        'price': '500.0',
        'paidPrice': '500.0',
        'currency': 'TRY',
        'basketId': 'B67832',
        'paymentGroup': 'PRODUCT',
        "callbackUrl": "http://127.0.0.1:8000/payment/result/",
        'buyer': buyer,
        'shippingAddress': address,
        'billingAddress': address,
        'basketItems': basket_items,
    }

    checkout_form_initialize = iyzipay.CheckoutFormInitialize().create(iyzico_request, options)
    content = checkout_form_initialize.read().decode('utf-8')
    json_content = json.loads(content)

    # Token'ı session'da sakla
    request.session['checkout_token'] = json_content['token']

    return HttpResponse(json_content['checkoutFormContent'])


@require_http_methods(['POST'])
@csrf_exempt
def result(request):
    token = request.session.get('checkout_token')
    if not token:
        messages.error(request, "Ödeme token bulunamadı. Lütfen tekrar deneyin.")
        return redirect('randevu_page')

    iyzico_request = {
        'locale': 'tr',
        'conversationId': '123456789',
        'token': token,
    }
    checkout_form_result = iyzipay.CheckoutForm().retrieve(iyzico_request, options)
    result_data = checkout_form_result.read().decode('utf-8')
    sonuc = json.loads(result_data, object_pairs_hook=list)

    status = next((v for k, v in sonuc if k == 'status'), None)

    # Mesajları durumlara göre sadece bir kez göster
    if status == 'success':
        messages.success(request, "Ödeme başarıyla gerçekleşti!")
    elif status == 'failure':
        messages.error(request, "Ödeme başarısız oldu. Lütfen tekrar deneyin.")
    else:
        messages.warning(request, "Bilinmeyen bir yanıt alındı.")

    # Token artık kullanılmayacak, session'dan sil
    if 'checkout_token' in request.session:
        del request.session['checkout_token']

    return redirect('randevu_page')


def success(request):
    return render(request, 'ok.html', {'success': 'İşlem Başarılı'})


def fail(request):
    return render(request, 'fail.html', {'fail': 'İşlem Başarısız'})