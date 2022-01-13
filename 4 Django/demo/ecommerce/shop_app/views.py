from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Cart, CartItem
from django.db.models import Q

def index(request):

    # sort products by ascending price
    # products = Product.objects.all().order_by('price')

    # sort all products by descending price
    products = Product.objects.all().order_by('-price')

    # category = Category.objects.get(title='jewelery')

    # find all categories in a list of values
    # categories = Category.objects.filter(title__in=['jewelery', 'electronics'])

    # filters can be chained
    # categories = Category.objects.filter(title__in=['jewelery', 'electronics']).filter(title__startswith='e')
    
    # find all the products whose categories list contains the title 'electronics'
    # other_model__field_name__lookup
    # products = Product.objects.filter(categories__title__icontains='electronics')

    # __lte is less than or equal to for the given field
    # products = Product.objects.filter(price__lte=100).order_by('price')

    # __gte is less than or equal to for the given field
    # products = Product.objects.filter(price__gte=100).order_by('price')

    # use __gte and __lte to search within a range
    # products = Product.objects.filter(price__gte=100, price__lte=200).order_by('price')

    # __startswith finds all items with whose value 
    # for a particular field starts with the given string
    # products = Product.objects.filter(title__startswith='f')

    # Q objects allow OR | and AND & operations with queries
    # products = Product.objects.filter(
    #     Q(title__startswith='f') | Q(title__startswith='s')
    # )

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


@login_required
def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)

    new_quantity = request.POST.get('quantity')

    cart_item.quantity = new_quantity

    cart_item.save()

    return redirect(reverse('users_app:detail', kwargs={'username': request.user.username}))


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect(reverse('users_app:detail', kwargs={'username': request.user.username}))
