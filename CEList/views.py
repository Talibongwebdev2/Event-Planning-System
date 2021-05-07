from django.shortcuts import render, redirect
from django.http import HttpResponse
from CEList.models import Item, List


def home_page(request):
    items = Item.objects.all()
    return render(request, 'homepage.html',{'items' : items})  

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'customview.html', {'list': list_})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(nname =request.POST['namen'],nAddress=request.POST['nbirthdate'], list=list_)
    return redirect(f'/CEList/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(nitem=request.POST['itemn'],nprice =request.POST['pricen'],ndate =request.POST['daten'],list=list_)
    return redirect(f'/CEList/{list_.id}/')




