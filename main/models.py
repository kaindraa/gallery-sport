from django.db import models
import uuid  # tambahkan baris ini di paling atas
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    discount = models.FloatField()

