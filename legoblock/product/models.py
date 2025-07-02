from django.db import models

class ProductType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

from django.db import models

class Product(models.Model):
    DELIVERY_TYPE_CHOICES = [
        ('pickup', 'Pickup'),
        ('delivery', 'Delivery'),
        ('both', 'Pickup & Delivery'),
    ]

    name = models.CharField(max_length=100)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, blank=True)

    size_length = models.IntegerField(help_text="Урт (мм)")
    size_width = models.IntegerField(help_text="Өргөн (мм)")
    size_height = models.IntegerField(help_text="Өндөр (мм)")

    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    price_mnt = models.PositiveIntegerField(help_text="Үнэ (₮)")

    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True, null=True, help_text="Image URL")

    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    tags = models.CharField(max_length=255, blank=True, help_text="comma-separated")
    is_featured = models.BooleanField(default=False)

    delivery_type = models.CharField(max_length=10, choices=DELIVERY_TYPE_CHOICES, default='both')

    @property
    def image(self):
        return self.image_url

    def size_str(self):
        return f"{self.size_length}x{self.size_width}x{self.size_height} мм"

    def __str__(self):
        return self.name

