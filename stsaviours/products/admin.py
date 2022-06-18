from django.contrib import admin
from .models import Product


# ------ Products ------


class ProductAdmin(admin.ModelAdmin):
    """ Create admin views for Products """
    list_display = (
        "title",
        "price",
        "date_added",
    )
    search_fields = (
        "title",
        "description",
    )
    readonly_fields = ("slug", "thumbnail", "date_added")


# Register Product models
admin.site.register(Product, ProductAdmin)
