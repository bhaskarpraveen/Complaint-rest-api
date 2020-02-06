from django.db import models

# Create your models here.
class Primary(models.Model):
    category = models.CharField(max_length=30,null=True,blank=True)
    product_name = models.CharField(max_length=50,null=True,blank=True)
    product_brand = models.CharField(max_length=50,null=True,blank=True)

   
class Shop(Primary):
    shop_name = models.CharField(max_length=50,null=True,blank=True)
    street_name = models.CharField(max_length=50,null=True,blank=True)
    pin_code = models.CharField(max_length=50,null=True,blank=True)
    shop_details = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.shop_name

class Person(Primary):
    person_name = models.CharField(max_length=50,null=True,blank=True)
    person_phone = models.CharField(max_length=13,null=True,blank=True)
    person_details = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.person_name

class Online(Primary):
    online_name = models.CharField(max_length=50,null=True,blank=True)
    online_url = models.CharField(max_length=50,null=True,blank=True)
    online_details = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.online_name