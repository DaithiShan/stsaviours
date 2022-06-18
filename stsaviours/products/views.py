from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product

# ------ Product Page ------


def product_page(request, product):
    """
    Returns specified product
    """
    product = get_object_or_404(Product, slug=product)

    context = {
        'product': product
    }

    return render(request, 'products/product_page.html', context)