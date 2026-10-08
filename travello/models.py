from django.db import models

# Create your models here.

class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='uploads/destination/') #media/uploads/destination ==>address 
    desc = models.TextField()
    price = models.DecimalField(default= 0, decimal_places=2, max_digits=8)
    offer = models.BooleanField(default=False) 


    def __str__(self):
        return self.name