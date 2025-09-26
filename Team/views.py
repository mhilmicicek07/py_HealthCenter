from django.shortcuts import render
from .models import *
from News.models import News

# Create your views here.
def team_view(request):

    team = Team.objects.all()
    
    return render(request, 'Home/index.html', {
        'team': team,
    })

def team_detail_view(request,slug):

    news = News.objects.all()
    team = Team.objects.filter(slug=slug)

    return render(request, 'Team/team.html', {
        'team': team,
        'news': news,
    })