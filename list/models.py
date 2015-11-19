from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


class List(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now_add=True)

    @property
    def price(self):
        for items in self.item_set.all():
            total = 0.00
            total += float(items.price)
            return total

    def __str__(self):
        return self.title


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    description = models.TextField()
    image = models.URLField()
    list = models.ForeignKey(List)

    @property
    def reserved(self):
        total = self.pledge_set.aggregate(Sum('amount'))
        if len(self.pledge_set.all()) > 0:
            item_price = float(self.price)
            pledge_amount = float(total['amount__sum'])
            if item_price - pledge_amount <= 0:
                return True

        return False

    def __str__(self):
        return self.name


class Pledge(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    pledge_time = models.DateTimeField(auto_now_add=True)
