from django.contrib import admin

from .models import Product, ProductCategory, Order

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Order)
