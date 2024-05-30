from django.db import models

class ScrapedData(models.Model):
    source = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.source} - {self.product_name}"