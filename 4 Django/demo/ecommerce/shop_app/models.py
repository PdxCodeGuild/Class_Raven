from django.db import models
from django.contrib.auth import get_user_model
import random 
class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField() # price will be stored as pennies to avoid float rounding issues
    description = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=200)
    rating = models.FloatField(default=0.0)
    rating_count = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=random.randint(10,20))

    categories = models.ManyToManyField(Category, related_name='products')

    # return the price as a string $0.00
    def formatted_price(self):
        return f"${self.price / 100:.2f}"


    def __str__(self):
        return f"{self.title}"


class Cart(models.Model):
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='cart')
    products = models.ManyToManyField(Product, related_name='carts', blank=True)

    def __str__(self):
        return f"{self.owner}'s cart"