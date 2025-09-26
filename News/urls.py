from django.urls import path
from .views import *

urlpatterns = [
    path('', news_view, name='news_page'),
    path('<slug:slug>/', news_detail_view, name='news_detail_page'),
]
