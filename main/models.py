from django.db import models

#Ganti nama ke product
#Ganti gambar di readme
class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    discount = models.FloatField()
