from django.db import models

# Create your models here.
import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('sepatu', 'Sepatu'),
        ('jersey', 'Jersey'),
        ('bola', 'Bola'),
        ('tas', 'Tas'),
        ('kaoskaki', 'Kaos Kaki'),
        ('atribut', 'Atribut'),
    ]
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    stock = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name