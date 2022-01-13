from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem

def index(request):

    products = Product.objects.all()

    return render(request, 'shop/index.html', {'products': products})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = Cart.objects.get(owner=request.user)

    # create a CartItem to connect the product to the cart
    cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)

    # increase the quantity of this cart item in the cart
    cart_item.quantity += 1
    cart_item.save()

    return redirect(reverse('shop_app:index'))