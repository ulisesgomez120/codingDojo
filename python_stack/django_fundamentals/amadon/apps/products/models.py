from django.db import models
# Create your models here.
class ProductManager(models.Manager):
    pass
        

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
