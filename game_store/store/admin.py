from django.contrib import admin

from .models import Product, ProductCategory, Purchase

# Register your models here.
@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'icon']
    list_display = ('name', 'get_games_count',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'desc', 'thumb', 'image1', 'image2', 'category']
    list_display = ('name', 'get_category')


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    fields = ['user', 'product', 'amount', ]
    list_display = ('id', 'get_user', 'get_product', 'amount', 'get_price' )
