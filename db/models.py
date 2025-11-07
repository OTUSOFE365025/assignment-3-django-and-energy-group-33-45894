import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()


#Product model
class Product(models.Model):
    #make upc the primary key instead of ID
    upc = models.IntegerField(primary_key=True)
    #reuse name field for product names
    name = models.CharField(max_length=50, default="name")
    #float for price (force 2 decimal places and requires max_digits)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    #returns name upc
    #i.e. cheese 0000
    def __str__(self):
        return f"{self.name} ({self.upc})"

