from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.TextField(max_length=50)
    weight = models.TextField(max_length=50)
    price = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)