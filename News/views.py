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
    # Tek haber objesini alıyoruz:
    selected_news = get_object_or_404(News, slug=slug)
    # Diğer haberleri de al (footer veya sidebar için):
    other_news = News.objects.exclude(slug=slug)[:3]  # mesela 4 tanesini göstermek için

    return render(request, 'News/news.html', {
        'news_detail': selected_news,
        'other_news': other_news,
        'category': category,
    })