############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

# Seed a few products in the database
Product.objects.create(upc='1000', name='cream', price='2.99')
Product.objects.create(upc='2000', name='flour', price='5.99')
Product.objects.create(upc='3000', name='meat', price='12.79')

for p in Product.objects.all():
    print(f'UPC: {p.upc} \tName: {p.name} \t Price: {p.price}')
