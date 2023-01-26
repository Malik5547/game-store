import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='images', default="/thumb.png")

    def get_games_count(self):
        games = Product.objects.filter(category=self.id)
        return games.count()
    get_games_count.short_description = "Games"

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    desc = models.CharField(max_length=250)
    thumb = models.ImageField(upload_to='images')
    image1 = models.ImageField(upload_to='images', default=None)
    image2 = models.ImageField(upload_to='images', default=None)
    category = models.ForeignKey(ProductCategory, null=False, on_delete=models.CASCADE)

    def get_category(self):
        return self.category
    get_category.short_description = 'Category'


class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    amount = models.IntegerField(default=1)
    date = models.DateTimeField(default=datetime.datetime.now())

    def get_user(self):
        return self.user
    get_user.short_description = "User"

    def get_product(self):
        return self.product.name
    get_product.short_description = "Product"

    def get_price(self):
        return f"${self.price}"
    get_price.short_description = "Price"