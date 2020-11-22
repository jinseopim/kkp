from django.db import models


# Create your models here.
class StockSymbolCode(models.Model):
    stock_code = models.CharField(max_length=200, blank=True)
    stock_en_name = models.CharField(max_length=200, blank=True)
    stock_ko_name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.stock_code