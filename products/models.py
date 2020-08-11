from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    Hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    urls = models.URLField(max_length=50)
    image = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True)
    icon = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True)
    vote_total = models.IntegerField(default=1)
    is_published = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    modified_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:100]


class Vote(models.Model):
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.hunter
