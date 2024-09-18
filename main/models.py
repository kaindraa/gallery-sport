from django.db import models
import uuid  # tambahkan baris ini di paling atas


class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    discount = models.FloatField()

