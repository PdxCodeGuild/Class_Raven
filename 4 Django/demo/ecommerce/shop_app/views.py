from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Cart, CartItem
from django.db.models import Q
from django.core.paginator import Paginator

def index(request, page_num=1, per_page=5):


    # if URL parameters exist for page_num or per_page, use those values
    # otherwise, use the defaults from the index view
    page_num = request.GET.get('page_num') or page_num
    per_page = request.GET.get('per_page') or per_page


    # create a dictionary with the values from the form if they exist or defaults if they don't
    form = {
        'search_query': request.POST.get('search_query') or '',
        'order_by': request.POST.get('order_by') or 'price',
        'checked_categories': request.POST.getlist('categories') or [category.title for category in Category.objects.all()],
        'min_price': request.POST.get('min_price') or '',
        'max_price': request.POST.get('max_price') or '',
        'min_rating': request.POST.get('min_rating') or '',
        'max_rating': request.POST.get('max_rating') or '',
    }

    # pull the values from the form
    search_query = form.get('search_query')
    checked_categories = form.get('checked_categories')
    min_price = form.get('min_price')
    max_price = form.get('max_price')
    min_rating = form.get('min_rating')
    max_rating = form.get('max_rating')
    order_by = form.get('order_by')

    # get all products
    products = Product.objects.all()

    #
    # Apply all the filters based on which form fields had values when the form was submitted
    if search_query:
        # find the products whose title or description contain the search query
        products = products.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )

    # find only the products in the given categories
    products = products.filter(categories__title__in=checked_categories)


    # apply price filters
    if min_price and not max_price:
        # find products whose price is greater than the min
        products = products.filter(price__gte=min_price)

    if max_price and not min_price:
        # find products whose price is greater than the min
        products = products.filter(price__lte=max_price)

    if max_price and min_price:
        # find products whose price is greater than the min
        products = products.filter(price__gte=min_price, price__lte=max_price)


    # apply rating filters
    if min_rating and not max_rating:
        # find products whose price is greater than the min
        products = products.filter(rating__gte=min_rating)

    if max_rating and not min_rating:
        # find products whose price is greater than the min
        products = products.filter(rating__lte=max_rating)

    if max_rating and min_rating:
        # find products whose price is greater than the min
        products = products.filter(rating__gte=min_rating, rating__lte=max_rating)

    # sort the remaining products
    products = products.order_by(order_by)


    # create a page object from the remaining products
    products_page = Paginator(products, per_page).get_page(page_num)

    # print(products_page.num_pages)
    # print(products_page.page_range)

    # data for rendering 'categories' checkboxes and 'order by' select menu
    search_options = {
        'categories': [category.title for category in Category.objects.all()],
        'order_by_options': [
            {'label': 'Price (Low-to-High)', 'value': 'price'},
            {'label': 'Price (High-to-Low)', 'value': '-price'},
            {'label': 'Name (A-Z)', 'value': 'title'},
            {'label': 'Name (Z-A)', 'value': '-title'},
            {'label': 'Rating (Low-to-High)', 'value': 'rating'},
            {'label': 'Rating (High-to-Low)', 'value': '-rating'},
        ]
    }

    # pack it up in a dictionary and ship it to the template
    context = {
        'products_page': products_page,
        'search_options': search_options,
        'form': form
    }

    return render(request, 'shop/index.html', context)


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





#Queries
# sort products by ascending price
# products = Product.objects.all().order_by('price')

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