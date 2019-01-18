from django.db import models
from ..products.models import Product
# Create your models here.
class OrderManager(models.Manager):
    def total_price(self, data):
        price = Product.objects.get(id=data['prod_id']).price
        return str(price * int(data['quantity']))

class Order(models.Model):
    number = models.PositiveSmallIntegerField()
    products = models.ManyToManyField(Product, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = OrderManager()
