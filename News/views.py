from django.shortcuts import render, get_object_or_404
from .models import *

def news_view(request):
    news = News.objects.all()
    category = Category.objects.all()
    author = Author.objects.all()
    return render(request, 'Home/index.html', {
        'news': news,
        'category': category,
        'author': author,
    })

def news_detail_view(request, slug):
    category = Category.objects.all()
    selected_news = get_object_or_404(News, slug=slug)
    other_news = News.objects.exclude(slug=slug).order_by('-id')[:3]  # 3 son haber

    # Footer için tüm haberleri context'e ekleyelim
    return render(request, 'News/news.html', {
        'news_detail': selected_news,
        'selected_news': selected_news,  # footer template kontrolü için
        'other_news': other_news,
        'category': category,
        'latest_news': other_news,  # context processor yerine footer çalışsın
    })