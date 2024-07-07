
from django.db import models

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Categoty(models.Model):
    title = models.CharField(max_length=255)
    

class Products(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    last_update =models.DateTimeField(auto_now=True)
    inventory = models.IntegerField()
    category = models.ForeignKey(Categoty, on_delete=models.CASCADE, null=True)
    promotion = models.ManyToManyField(Promotion, blank=True)

