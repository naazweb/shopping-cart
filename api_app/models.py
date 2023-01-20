from django.db import models


class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        # Send Email
        return 
