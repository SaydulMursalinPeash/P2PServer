from django.db import models

class Method(models.Model):
    name=models.CharField(max_length=300,null=False,blank=False,unique=True)
    symbol=models.CharField(max_length=50,null=False,blank=False,unique=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    icon=models.ImageField(upload_to='payment/method/')

    def __str__(self):
        return self.name
