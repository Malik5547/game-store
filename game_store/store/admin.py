from django.contrib import admin

from .models import Product, ProductCategory, Purchase

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name',]
    list_display = ('name',)


admin.site.register(ProductCategory, CategoryAdmin)
admin.site.register(Product)
admin.site.register(Purchase)
