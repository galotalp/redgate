from django.contrib import admin
from django.urls import path
from .views import index, hiddenpage, drummer, gal

urlpatterns = [
    path('', index, name='index'),
    path('mcleod', hiddenpage, name='Mariessas Hidden Page'),
    path('drummer', drummer, name='Dans Page'),
    path('gal', gal, name='Gals page'),

    
]
