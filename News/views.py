from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def news_view(request):

    news =  News.objects.all()
    category = Category.objects.all()
    author = Author.objects.all()
    return render(request, 'Home/index.html', {
        'news': news,
        'category':category,
        'author': author,
    })

def news_detail_view(request,slug):

    category = Category.objects.all()
    news = News.objects.filter(slug=slug)
    #! #TODO: haber detay sayfasına girildiğinde footerdaki haber bilgisi ile detay haber bilgisi aynı ve diğer haberler görünmüyor.
    return render(request, 'News/news.html', {
        'news': news,
        'category':category,
    })