from django.urls import path
from .views import fail, payment, result, success

urlpatterns = [
    path('', payment, name='ödeme_page'),
    path('ok/', success, name='success'),
    path('fail/', fail, name='fail'),
    path('result/', result, name='result'),
]
