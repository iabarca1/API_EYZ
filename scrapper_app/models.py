# scrapper_app/models.py

from django.db import models

class ScrapedData(models.Model):
    source = models.CharField(max_length=100)
    product_name = models.CharField(max_length=255)
    price = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.source} - {self.product_name}"
