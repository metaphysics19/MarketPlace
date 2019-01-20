from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


class Products(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    price = models.FloatField()
    image = models.ImageField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
    category = models.CharField(max_length=100)
    name = models.ForeignKey(Products, on_delete=models.CASCADE)


class Comments(models.Model):
    comment = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
