
from django.db import models
from product.models import Product

class Order(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

    delivery_address = models.TextField()
    notes = models.TextField(blank=True)
    shipping_method = models.CharField(max_length=100, blank=True)
    payment_method = models.CharField(max_length=100, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

    def __str__(self):
        return f"Order #{self.id} - {self.full_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price_mnt * self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"
