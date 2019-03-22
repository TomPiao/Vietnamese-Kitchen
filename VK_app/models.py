from django.db import models

# Create your models here.
class ItemType(models.Model):
    type_name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.type_name

class MenuItem(models.Model):
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    item_code = models.CharField(max_length=128, unique=True)
    item_name = models.CharField(max_length=256)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name
