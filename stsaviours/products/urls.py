from django.urls import path
from .views import product_page

urlpatterns = [
    path(
        "shop/<slug:product>",
        product_page,
        name="product_page",
    ),
]