from django.shortcuts import get_object_or_404, render
from .models import Team
from News.models import News

# Create your views here.
def team_view(request):

    team = Team.objects.all()
    
    return render(request, 'Team/team.html', {
        'team': team,
    })

def team_detail_view(request,slug):

    news = News.objects.all()
    member = get_object_or_404(Team, slug=slug)

    return render(request, 'Team/team.html', {
        'team': [member],
        'news': news,
    })
