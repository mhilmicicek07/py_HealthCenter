from django.shortcuts import render
from .models import News

def latest_news(request):
    """Footer'da görünmesi için son haberleri döndürür."""
    return {
        'latest_news': News.objects.order_by('-id')[:3]
    }