from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Goods(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=155)
    photo_video = models.FileField(upload_to='users/', blank=True)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    availability = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0)
    reviews = models.TextField(blank=True)
    warranty = models.CharField(max_length=100, blank=True)
    season = models.CharField(max_length=50, blank=True)
    size = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title




