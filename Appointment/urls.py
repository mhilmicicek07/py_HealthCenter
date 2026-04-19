from django.urls import path
from .views import randevu_view

urlpatterns = [
    path('', randevu_view, name='randevu_page')
]
