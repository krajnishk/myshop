from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('name',)

    def __str__(self):
        """Unicode representation of Category."""
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    """Model definition for Product."""

    # TODO: Define fields here
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        """Unicode representation of Product."""
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
