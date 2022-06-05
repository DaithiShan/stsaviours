from django.contrib import admin
from .models import (
    Category,
    Subcategory,
    Product,
)

# ------ Product Categories ------


class CategoryAdmin(admin.ModelAdmin):
    """ Create admin views for Categories """
    list_display = ("title", "ordering")
    search_fields = ("title", "ordering")


class SubcategoryAdmin(admin.ModelAdmin):
    """ Create admin views for Subcategories """
    list_display = ("title", "parent", "ordering")
    search_fields = ("title", "parent__title", "ordering")


# ------ Products ------


class ProductAdmin(admin.ModelAdmin):
    """ Create admin views for Products """
    list_display = (
        "title",
        "category",
        "subcategory",
        "price",
        "date_added",
    )
    search_fields = (
        "title",
        "category__title",
        "subcategory__title",
        "description",
    )
    readonly_fields = ("slug", "thumbnail", "date_added")


# Register Category, Subcategory and Product models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
