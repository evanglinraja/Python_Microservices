from django.shortcuts import render,redirect
import requests
from django.conf import settings

API_URL = settings.API_GATEWAY_URL + 'orders/'

def order_list(request):
    response = requests.get(API_URL)
    orders= response.json() if response.status_code == 200 else []
    return render(request, 'order/order_list.html', {'orders': orders})

def order_create(request):
    if request.method == 'POST':
        payload = {
            'ProductId': request.POST["ProductId"],
            'Quantity': request.POST["Quantity"],
            'TotalPrice': request.POST["TotalPrice"],
        }
        response=requests.post(API_URL,json=payload)
        if response.status_code == 200:  
            return redirect('order_list')
    return render(request, 'order/order_create.html')

def order_edit(request, order_id):
    URL=API_URL + str(order_id)
    response = requests.get(URL)
    order=(response.json())
    if request.method == 'POST':
        payload = {
            'ProductId': request.POST["ProductId"],
            'Quantity': request.POST["Quantity"],
            'TotalPrice': request.POST["TotalPrice"],
        }
        response=requests.put(URL,json=payload)
        if response.status_code == 200:  
            return redirect('order_list')
    return render(request, 'order/order_edit.html', {'order': order})

def order_delete(request, order_id):
    URL=API_URL + str(order_id)
    if request.method == 'POST':
        response=requests.delete(URL)
        if response.status_code == 200:  
            return redirect('order_list')
    return redirect('order_list')

