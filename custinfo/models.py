from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=1)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zipcode=models.IntegerField()
    state=models.CharField(max_length=100)
    mobile=models.IntegerField()

def __str__(self):
    return str(self.id)


