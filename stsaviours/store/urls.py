from django.contrib import admin
from django.urls import path
from .views import home, shop, search

urlpatterns = [
    path('', home, name='store-home'), 
    path('shop/', shop, name='shop'),
    path('shop/<slug:product>/', shop, name='shop'),
    path('search', search, name='search'),
]
