from django.http import HttpResponse
from django.shortcuts import render

from .models import ProductCategory

# Create your views here.
def index(request):
    categories = ProductCategory.objects.order_by('name')
    context = {
        'categories_list': categories,
    }
    return render(request, 'store/index.html')


def product(request, product_id):
    return HttpResponse(f"This is product {product_id}")