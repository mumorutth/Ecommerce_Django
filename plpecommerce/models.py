from django.db import models

# Create your models here.
class Product(models.model):
    name = models.CharField(max_length=400)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='products/')
    #add more fields