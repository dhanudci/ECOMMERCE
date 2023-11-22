from django.db import models
from django.contrib.auth.models import User

STATE_CHOICES = (
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Andhra pradesh','Andhra pradesh'),
    ('Arunachal pradesh','Arunachal pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('chattisgarh','chattisgarh'),
    ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
    ('Daman and Diu','Daman and Diu'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujrat','Gujrat'),
    ('Haryana','Haryana'),
    ('Himachal pradesh','Himachal pradesh'),
    ('Jammu & kashmir','Jammu & kashmir'),
    ('Odisa','Odisa'),
    ('Tamilnadu','Tamilnadu'),
    ('Tripura','Tripura'),
    ('Uttar pradesh','Uttar pradesh')
)

CATEGORY_CHOICES =(
    ('CR','Curd'),
     ('ML','Milk'),
      ('LS','Lassi'),
       ('MS','Milkshake'),
        ('PN','Paneer'),
         ('GH','Ghee'),
          ('CZ','Cheese'),
           ('IC','Ice-Creams'),
)

class product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition=models.TextField(default='')
    prodapp=models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_images=models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name

