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


# This model will be used as a "through table" between Carts and their Products
# to allow multiples of each product in a cart with the 'quantity' attribute
class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=0)

class Cart(models.Model):
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='cart')
    
    # through=CartItem will leverage the 'cart' and 'product' ForeignKey fields
    # to allow multiples of a product to be added to a cart
    products = models.ManyToManyField(Product, through=CartItem, related_name='carts', blank=True)

    # return the sum of the quantities of the cart_items in the cart
    def item_count(self):
        count = 0
        for cart_item in self.cart_items.all():
            count += cart_item.quantity

        return count

        # the above loop as a list comprehension :D
        # return sum([cart_item.quantity for cart_item in self.cart_items.all()])

        

    def __str__(self):
        return f"{self.owner}'s cart"