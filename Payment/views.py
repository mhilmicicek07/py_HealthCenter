from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponse
import iyzipay
import json

# İyziPay API bilgileri (sandbox veya production)
options = {
    'api_key': 'sandbox-4pXMNqLNKKyHdjhPdsAOpgsJt3wlOSqU',
    'secret_key': 'sandbox-z9a7giJpDFJBemWw5l6HZVEPGvbGa9lk',
    'base_url': 'sandbox-api.iyzipay.com',
}


@csrf_exempt
def payment(request):
    """
    Ödeme formunu oluşturur ve kullanıcıya gösterir.
    """
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
        'ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
        'city': 'Istanbul',
        'country': 'Turkey',
        'zipCode': '34732',
    }

    address = {
        'contactName': 'Jane Doe',
        'city': 'Istanbul',
        'country': 'Turkey',
        'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'zipCode': '34732',
    }

    basket_items = [
        {
            'id': 'BI101',
            'name': 'Randevu Ücreti',
            'category1': 'Sağlık',
            'itemType': 'VIRTUAL',
            'price': '500.00',
        }
    ]

    request_data = {
        'locale': 'tr',
        'conversationId': '123456789',
        'price': '500.00',
        'paidPrice': '500.00',
        'currency': 'TRY',
        'basketId': 'B67832',
        'paymentGroup': 'PRODUCT',
        'callbackUrl': request.build_absolute_uri('/payment/result/'),
        'buyer': buyer,
        'shippingAddress': address,
        'billingAddress': address,
        'basketItems': basket_items,
    }

    try:
        checkout_form = iyzipay.CheckoutFormInitialize().create(request_data, options)
        response = json.loads(checkout_form.read().decode('utf-8'))

        token = response.get('token')
        form_content = response.get('checkoutFormContent', '')

        if not token:
            messages.error(request, "Ödeme başlatılamadı. Lütfen tekrar deneyin.")
            return redirect('randevu_page')

        # Token'ı session'da sakla
        request.session['checkout_token'] = token

        return HttpResponse(form_content)

    except Exception as e:
        messages.error(request, f"Ödeme sırasında bir hata oluştu: {str(e)}")
        return redirect('randevu_page')


@require_http_methods(['POST'])
@csrf_exempt
def result(request):
    """
    Ödeme sonucu callback endpoint'i.
    """
    token = request.session.get('checkout_token')
    if not token:
        messages.error(request, "Geçersiz veya süresi dolmuş ödeme isteği.")
        return redirect('randevu_page')

    request_data = {
        'locale': 'tr',
        'conversationId': '123456789',
        'token': token,
    }

    try:
        result_obj = iyzipay.CheckoutForm().retrieve(request_data, options)
        result_json = json.loads(result_obj.read().decode('utf-8'))

        status = result_json.get('status')
        payment_id = result_json.get('paymentId')
        error_message = result_json.get('errorMessage')

        if status == 'success':
            messages.success(request, "Ödeme başarıyla tamamlandı. Randevunuz oluşturuldu.")
        else:
            messages.error(request, f"Ödeme başarısız oldu: {error_message or 'Bilinmeyen hata'}")

    except Exception as e:
        messages.error(request, f"Ödeme sonucu alınamadı: {str(e)}")

    finally:
        # Token temizleniyor
        request.session.pop('checkout_token', None)

    return redirect('randevu_page')


def success(request):
    return render(request, 'ok.html', {'success': 'İşlem Başarılı'})


def fail(request):
    return render(request, 'fail.html', {'fail': 'İşlem Başarısız'})