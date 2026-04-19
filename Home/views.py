from django.shortcuts import render
from News.models import Author, Category, News
from Team.models import Team
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
