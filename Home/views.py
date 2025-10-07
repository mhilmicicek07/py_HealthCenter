from django.shortcuts import render,redirect
from News.models import *
from News.views import news_view
from Team.models import *
from Team.views import team_view
from Appointment.forms import RandevuForm

# Create your views here.

def index_view(request):

    news =  News.objects.all()
    category = Category.objects.all()
    author = Author.objects.all()
    team = Team.objects.all()
    form = RandevuForm()
    
    return render(request, 'Home/index.html', {
        'news': news,
        'category':category,
        'author': author,
        'team':team,
        'form': form,
    })