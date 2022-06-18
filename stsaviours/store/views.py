from django.shortcuts import render
from django.db.models import Q
from products.models import Product

# ---- Landing Page View -----


def home(request):
    """
    Landing/Welcome page for website
    """
    return render(request, 'store/index.html')


# ---- Shop View -----


def shop(request):
    """
    Main shop page list of available products
    """
    context = {}
    q = Q()

    # product
    order = request.GET.get("order_by") or "ordering"  # '?order_by=*param'
    products = Product.objects.filter(q)

    # Product List
    context["products"] = products

    return render(request, 'store/shop.html', context)


# Custom search view adapted from Boutique Ado Mini Project


def search(request):
    """
    Search functionality separated to own page.
    Returns search results
    """
    query = None
    context = {}
    q = Q()

    # text search
    if "q" in request.GET:
        query = request.GET.get("q")

        q &= (
            Q(title__icontains=query)
        )

    # product
    products = Product.objects.filter(q)

    context["products"] = products
    context["search_term"] = query

    return render(request, 'store/search_shop.html', context)
