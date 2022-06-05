from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models
from django.template.defaultfilters import slugify


# ------ Product Categories ------


class Category(models.Model):
    """
    Defines category of selected product
     (for filtering purposes)
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ("ordering", "title")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Overwrite default save and create product slug
        """
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Subcategory(models.Model):
    """
    Defines subcategory of selected product
     (for filtering purposes)
    """
    parent = models.ForeignKey(Category,
                               related_name='subcategories',
                               blank=True,
                               null=True,
                               on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Subcategories"
        ordering = ("parent", "ordering", "title")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# ------ Products ------


class Product(models.Model):
    """ Defines all products """
    category = models.ForeignKey(Category,
                                 blank=True,
                                 null=True,
                                 related_name='products',
                                 on_delete=models.SET_NULL)
    subcategory = models.ForeignKey(Subcategory,
                                    blank=True,
                                    null=True,
                                    related_name='subcategory',
                                    on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    ordering = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField(default=15)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    thumbnail = models.ImageField(
        upload_to="products/thumbnails/", blank=True, null=True
    )

    class Meta:
        """
        Products sorted by title
        ref: https://tinyurl.com/3v38mtn5
        """
        ordering = ("ordering", "title")

    def __str__(self):
        return self.title

    def make_thumbnail(self, image, size=(250, 250)):
        """
        Method which automatically makes thumbnail images
        of the main uploaded image, reducing size to 300x300
        """
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, "JPEG", quality=85)
        thumbnail = File(thumb_io, name=image.name.replace("products/", ""))
        return thumbnail

    def save(self, *args, **kwargs):
        """
        Modified save method to update thumbnail only if object is
        new, or the object image has been updated
        """
        if self.pk is None:
            self.thumbnail = self.make_thumbnail(self.image)
        else:
            original = Product.objects.get(id=self.pk)
            if original.image != self.image:
                self.thumbnail = self.make_thumbnail(self.image)
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_product_url(self):
        """
        Creates a redirect url for product
        based on whether products has a set type or not
        """
        url = f"/shop/{self.category.slug}/{self.subcategory.slug}/"
        return (
            url + f"{self.slug}"
        )
