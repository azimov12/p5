from django.shortcuts import render
from .views import sweets, meat, clothes, details
from django.urls import path

urlpatterns = [
    path('sweet/', sweets),
    path('meat/', meat),
    path('clothes/', clothes),
    path('details<int:market_id>/', details)
]