
from django.urls import path,include
from .views import anasayfa

urlpatterns = [
    
    path('', anasayfa, name='anasayfa'),
]
