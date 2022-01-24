from django.core.management.base import BaseCommand
import requests

from shop_app.models import Product, Category

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        
        Product.objects.all().delete()
        Category.objects.all().delete()

        # get the data from the api
        url = 'https://fakestoreapi.com/products'
        response = requests.get(url)

        products = response.json()


        # create a database entry for each product
        for product in products:
            title = product['title']
            price = float(product['price'])
            description = product['description']
            category = product['category']
            rating = float(product['rating']['rate'])
            rating_count = int(product['rating']['count'])
            image_url = product['image']

            # create an entry in the Category database if the given category 
            # doesnt exist yet, otherwise use the existing entry
            # x,y = (2,4) # tuple unpacking
            # category, created = (category_object, boolean)
            category, created = Category.objects.get_or_create(title=category)

            # create the Product entry
            product = Product.objects.create(
                title=title,
                price=price,
                description=description,
                rating=rating,
                rating_count=rating_count,
                image_url=image_url
            )

            # add the category to the products list of categories
            product.categories.add(category)