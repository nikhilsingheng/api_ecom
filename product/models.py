from distutils.command.upload import upload
from statistics import quantiles
from django.db import models
from datetime import datetime
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=300)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Store(models.Model):
    userId = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    title = models.CharField(max_length=500)
    # discription = models.CharField(max_length=500)
    storeID = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    conition = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class ProductImg(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)


class Cart(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    quantiles = models.IntegerField()


class CartItem(models.Model):
    cartId = models.ForeignKey(Cart, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantiles = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    return "%s/%s.%s"("img", datetime.now(), ext)


class FileUploded(models.Model):
    imgFild = models.ImageField(upload_to=upload_location)
