from django.db import models
from datetime import datetime


class Product(models.Model):
    x = [
        ('phone','phone'),
        ('computer','computer'),
        ('ipad','ipad'),
        ('playstation','playstation'),
    ]
    name = models.CharField(max_length=50, default='megzz', verbose_name='title')
    content = models.TextField(null=True, blank=True, verbose_name='Description')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10.0)
    image = models.ImageField(upload_to='photos/%y/%m/%d', height_field=None, width_field=None, max_length=None)
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50, null=True, blank=True, choices=x)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-name']



class Test(models.Model):
    
    date = models.DateField()
    time = models.TimeField(null=True)
    created = models.DateTimeField(null=True, default=datetime.now)