from django.shortcuts import render
import iyzipay
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


api_key = 'sandbox-4pXMNqLNKKyHdjhPdsAOpgsJt3wlOSqU'
secret_key = 'sandbox-z9a7giJpDFJBemWw5l6HZVEPGvbGa9lk'
base_url = 'sandbox-api.iyzipay.com'

options = {
    'api_key': api_key,
    'secret_key': secret_key,
    'base_url': base_url,
}

sozlukToken = list()

# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

def index(request):
    context = dict()
    context['mesaj'] = 'Django ile iyzico ödeme entegrasyonu'
    template = 'Appointment/appointment.html'

    return render(request, template, context)

@csrf_exempt
def payment(request):
    context = dict()
    buyer={
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

    address={
        'contactName': 'Jane Doe',
        'city': 'Istanbul',
        'country': 'Turkey',
        'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'zipCode': '34732'
    }

    basket_items=[
        {
            'id': 'BI101',
            'name': 'Binocular',
            'category1': 'Collectibles',
            'category2': 'Accessories',
            'itemType': 'PHYSICAL',
            'price': '0.3'
        },
        {
            'id': 'BI102',
            'name': 'Game code',
            'category1': 'Game',
            'category2': 'Online Game Items',
            'itemType': 'VIRTUAL',
            'price': '0.5'
        },
        {
            'id': 'BI103',
            'name': 'Usb',
            'category1': 'Electronics',
            'category2': 'Usb / Cable',
            'itemType': 'PHYSICAL',
            'price': '0.2'
        }
    ]

    request={
        'locale': 'tr',
        'conversationId': '123456789',
        'price': '1',
        'paidPrice': '1.2',
        'currency': 'TRY',
        'basketId': 'B67832',
        'paymentGroup': 'PRODUCT',
        "callbackUrl": "http://127.0.0.1:8000/result/", #! #TODO: payment olunca sorun yok ama result olunca çalışmıyor, appointment,home olunca da csrf token hatası veriyor.
        "enabledInstallments": ['2', '3', '6', '9'],    
        'buyer': buyer,
        'shippingAddress': address,
        'billingAddress': address,
        'basketItems': basket_items,
        # 'debitCardAllowed': True
    }
    checkout_form_initialize = iyzipay.CheckoutFormInitialize().create(request,options)
    page = checkout_form_initialize
    # print('iyzico-sayfa')
    # print(page)
    # print('*'*50)
    content = checkout_form_initialize.read().decode('utf-8')
    # print(content)
    # print(type(content))
    # print('*'*50)
    json_content = json.loads(content)
    # print('*'*50)
    # print(json_content['checkoutFormContent'])
    # print('*'*50)
    # print(json_content['token'])
    # print('*'*50)
    sozlukToken.append(json_content['token'])
    return HttpResponse(json_content['checkoutFormContent'])

@require_http_methods(['POST'])
@csrf_exempt
def result(request):
    context = dict()

    url = request.META.get('index')

    request = {
        'locale':'tr',
        'conversationId':'123456789',
        'token': sozlukToken[0],
    }
    checkout_form_result = iyzipay.CheckoutForm().retrieve(request,options)
    # print('*'*50)
    # print('sonuc')
    # print(type(checkout_form_result))
    # print('*'*50)
    # print(sozlukToken[0])
    result = checkout_form_result.read().decode('utf-8')
    sonuc = json.loads(result,object_pairs_hook=list)
    # print('sonuc')
    # print(sonuc[0][1])
    # print(sonuc[5][1])
    for i in sonuc:
        print(i)
    # print('*'*50)
    # print('sozluk_token')
    # print(sozlukToken)
    # print('*'*50)

    if sonuc[0][1] == 'success':
        context['success'] = 'Başarılı İşlem'
        return HttpResponseRedirect(reverse('success'),context)
    elif sonuc[0][1] == 'failure':
        context['failure'] = 'Başarısız İşlem'
        return HttpResponseRedirect(reverse('failure'),context)
    
    return HttpResponse(url)

def success(request):
    context = dict()
    context['success'] = 'İşlem Başarılı'
    template = 'ok.html'

    return render(request,template,context)

def fail(request):
    context = dict()
    context['fail'] = 'İşlem Başarısız'
    template = 'fail.html'

    return render(request,template,context)
