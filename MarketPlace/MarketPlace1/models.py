from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Products(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    price = models.FloatField()
    image = models.ImageField()
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def publish(self):
        self.date_posted = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products_detail', kwargs={'pk': self.pk})
            

class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Comments(models.Model):
    comment = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
