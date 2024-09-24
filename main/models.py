from django.db import models
import uuid  # tambahkan baris ini di paling atas
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    discount = models.FloatField()

