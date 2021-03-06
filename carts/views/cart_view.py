
# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Min

# Models
from carts.models import Cart
from products.models import Product

# Utils
from core.utils import random_pk_list


@login_required
def cart_view(request):
    """Cart view"""
    try:
        cart_products = request.user.cart.cartproduct_set.all()
    except Cart.DoesNotExist:
        cart_products = None

    products = Product.objects.filter(
        id__in=random_pk_list(Product, 3),
        is_active=True
    ).exclude(
        image=''
    ).values(
        'id', 'name', 'image', 'provider__id',
        'provider__name', 'price_default'
    ).annotate(Min('productprice__hierarchy'))

    return render(request, 'carts/cart.html', {
        'cart_products': cart_products,
        'products': products,
    })
