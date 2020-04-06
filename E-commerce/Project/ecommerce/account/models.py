from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):   
    name = models.CharField(blank=False, max_length=120, unique=True)
    phone_number = models.CharField(max_length=10, unique=True) 
    
    def __unicode__(self): 
        return self.name 

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField(default=0, unique=False)
    image = models.ImageField(upload_to ='products/',blank=True) 

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', null=True, blank=True,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='orders', null=True, blank=True,on_delete=models.CASCADE,)
    order_date = models.DateField(auto_now=True)
    quantity = models.IntegerField()