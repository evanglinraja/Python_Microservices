from django.shortcuts import render,redirect
from django.conf import settings
import requests

API_URL = settings.API_GATEWAY_URL + 'products/'

def product_list(request):
    response = requests.get(API_URL)
    products= response.json() if response.status_code == 200 else []
    print(products)
    return render(request, 'product/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        payload = {
            'Name': request.POST.get('Name'),
            'Price': request.POST.get('Price'),
            'Stock': request.POST.get('Stock'),
        }
        response=requests.post(API_URL,json=payload)
        if response.status_code == 200:  
            return redirect('product_list')
    return render(request, 'product/product_create.html')

def product_edit(request, product_id):
    URL=API_URL + str(product_id)
    response = requests.get(URL)
    product=(response.json())
    if request.method == 'POST':
        payload = {
            'Name': request.POST.get('Name'),
            'Price': request.POST.get('Price'),
            'Stock': request.POST.get('Stock'),
        }
        response=requests.put(URL,json=payload)
        if response.status_code == 200:  
            return redirect('product_list')
    return render(request, 'product/product_edit.html', {'product': product})

def product_delete(request, product_id):
    URL=API_URL + str(product_id)
    if request.method == 'POST':
        response=requests.delete(URL)
        if response.status_code == 200:  
            return redirect('product_list')
    return redirect('product_list')


