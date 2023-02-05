from django.db import models
from django.contrib.auth.models import User

class App(models.Model):
    firts_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    date_birth = models.DateField(null=True)
    email = models.EmailField()
    dni = models.CharField(max_length=32)
    address = models.CharField(max_length=256)

    #def __str__(self):
    #    return 


class Device_costumer(models.Model):
    color =  models.CharField(max_length=128)
    type_device =  models.CharField(max_length=128)
    brand =  models.CharField(max_length=128)
    model =  models.CharField(max_length=128)

    #def __str__(self):
    #    return 


class Producto_sale(models.Model):
    name_product =  models.CharField(max_length=128)
    delivery_date = models.DateField(null=True)  

    #def __str__(self):
    #    return 

