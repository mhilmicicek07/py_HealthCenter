from django.urls import path
from .views import *

urlpatterns = [
    path('', team_view, name='team_page'),
    path('<slug:slug>/', team_detail_view, name='team_detail_page'),
]
