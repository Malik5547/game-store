from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import  get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from .forms import RegistrationForm, LoginForm
from .models import ProductCategory, Product, Purchase
from .serializers import UserSerializer, UserModel


PRODUCTS_ON_PAGE = 4


# Create your views here.
def index(request):
    categories = ProductCategory.objects.order_by('name')
    all_products = Product.objects.order_by('id')

    p = Paginator(all_products, PRODUCTS_ON_PAGE)
    page = request.GET.get('page')
    page_products = p.get_page(page)

    context = {
        'categories_list': categories,
        'product_list': all_products,
        'products': page_products,
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

    p = Paginator(products_by_cat, PRODUCTS_ON_PAGE)
    page = request.GET.get('page')
    page_products = p.get_page(page)

    context = {
        'categories_list': categories,
        'selected_cat': cat,
        'products': page_products,
    }

    return render(request, 'store/index.html', context)


def product(request, product_id):
    crt_product = Product.objects.get(id=product_id)

    context = {
        'product': crt_product,
    }

    if request.method == 'POST':
        user = request.user
        amount = int(request.POST['amount'])

        if user.is_authenticated:
            new_purchase = Purchase(user_id=user, product_id=crt_product, price=crt_product.price * amount, amount=amount)
            new_purchase.save()

            messages.success(request, f'Success! You bought {crt_product.name}')
            return render(request, 'store/product.html', context)

        else:
            messages.error(request, f'To buy a product you should first sign in.')
            return redirect('store:sign-in')
    else:

        return render(request, 'store/product.html', context)


def purchases(request):
    user = request.user

    if user.is_authenticated:
        user_purchases = Purchase.objects.filter(user_id=user)
        context = {
            "purchases": user_purchases,
        }

        return render(request, 'store/purchases.html', context)

    else:
        messages.error(request, f'To see your purchases, you must first log in.')
        return redirect('store:sign-in')


# REST Framework
class UsersViewSet(viewsets.ViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = UserModel.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrive(self, request, pk=None):
        user = get_object_or_404(UserModel, pk=pk)
        serializers = UserSerializer(user)
        return Response(serializers.data)