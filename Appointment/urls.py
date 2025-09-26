from django.urls import path
from .views import *
from Payment.urls import *

urlpatterns = [
    path('', randevu_view, name='randevu_page')
]
