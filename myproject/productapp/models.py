from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length= 100)
    weight = models.IntegerField
    price = models.FloatField
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')