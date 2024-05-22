from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Products
# Create your views here.

def index(request):
    products = Products.objects.all()
    return render(request, 'product/products.html', 
                  {
                      "products": products
                  })

def create(request):

    if request.method == 'POST':
        print(request.POST)

        new_product = Products(name=request.POST['add-name'], description=request.POST['add-description'], price=request.POST['add-price'])
        new_product.save()

        return HttpResponseRedirect(reverse('products'))

    return render(request, 'product/create_product.html')

def product_detail(request, id):
    product_detail = Products.objects.get(pk=id)
    return render(request, 'product/detail_product.html', 
                  {
                      "product_detail":product_detail
                  })

