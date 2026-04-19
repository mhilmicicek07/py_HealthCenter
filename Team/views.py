from django.shortcuts import get_object_or_404, render
from .models import Team
from News.models import News


def team_view(request):
    team = Team.objects.all()
    news = News.objects.order_by('-tarih')

    return render(request, 'Team/team.html', {
        'team': team,
        'news': news,
    })


def team_detail_view(request, slug):
    news = News.objects.order_by('-tarih')
    member = get_object_or_404(Team, slug=slug)

    return render(request, 'Team/team.html', {
        'team': [member],
        'news': news,
    })
