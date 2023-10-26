from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    stock = models.IntegerField()
    category = models.CharField(max_length=100)
