# properties/models.py
from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    city = models.CharField(max_length=100)
    lat = models.FloatField()  # خط العرض
    lng = models.FloatField()  # خط الطول
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
