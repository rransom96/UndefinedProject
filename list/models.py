from django.contrib.auth.models import User
from django.db import models


class List(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now_add=True)

    @property
    def price(self):
        for items in self.item_set.all():
            total = 0.00
            total += items.price
            return total


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    description = models.TextField()
    image = models.URLField()
    list = models.ForeignKey(List)

    # def reserved(self):
    #     if self.price -


# class Pledge(models.Model):
#