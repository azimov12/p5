from django.urls import path
from django.http import HttpResponse
# Create your views here.

def sweets(request):
    return HttpResponse('This is place of sweets')

def meat(request):
    return HttpResponse('This is place of meat')    

def clothes(request):
    return HttpResponse('This is plase of clothes')

def details(request, market_id):
    return HttpResponse(f'It is market {market_id}')    