import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    desc = models.CharField(max_length=250)
    thumb = models.ImageField(upload_to='images')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    amount = models.IntegerField(default=1)
    date = models.DateTimeField(default=datetime.datetime.now())