from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse
from .models import Item, Purchase

def greetings(request):
    return HttpResponse("Добро пожаловать в наш магазин!")

def list_item(request):
    items= Item.objects.all()
    contex = {
        'items':items,
    }
    return render(request, 'list_item.html', contex)

def detail_item(request, item_id):

    item = Item.objects.get(id=item_id)
    contex = {
        'item':item,
    }
    return render(request, 'detail_item.html', contex)


