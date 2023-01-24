from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import RegistrationForm, LoginForm
from .models import ProductCategory, Product

# Create your views here.
def index(request):
    categories = ProductCategory.objects.order_by('name')
    products = Product.objects.order_by('id')
    context = {
        'categories_list': categories,
        'product_list': products,
    }
    return render(request, 'store/index.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()

    return render(request, 'store/sign_up.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            print("User logged.")

            return redirect('/')

        print("Wrong credentials.")
    else:
        form = LoginForm()

    return render(request, 'store/sign_in.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('/')


def category(request, cat_id):
    categories = ProductCategory.objects.order_by('name')
    products_by_cat = Product.objects.filter(category=cat_id)
    cat = ProductCategory.objects.get(id=cat_id)

    context = {
        'categories_list': categories,
        'selected_cat': cat,
        'product_list': products_by_cat,
    }

    return render(request, 'store/index.html', context)


def product(request, product_id):
    selected_product = Product.objects.get(id=product_id)

    context = {
        'product': selected_product,
    }

    return render(request, 'store/product.html', context)