from django.http import HttpResponse
from django.shortcuts import render

from .models import ProductCategory, Product

# Create your views here.
def index(request):
    categories = ProductCategory.objects.order_by('name')
    products = Product.objects.order_by('id')[:6]
    context = {
        'categories_list': categories,
        'product_list': products,
    }
    return render(request, 'store/index.html', context)


def product(request, product_id):
    return HttpResponse(f"This is product {product_id}")