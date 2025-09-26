from django.urls import path
from .views import *
from News.urls import *

urlpatterns = [
    path('', index_view, name='index_page'),
]
