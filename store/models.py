from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200),
    cost = models.DecimalField(max_digits=10, decimal_places=2),

