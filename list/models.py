from datetime import date
from christmas_list.settings import STRIPE_API_KEY
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
import stripe


class List(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    deadline = models.DateField(default=date.today)
    inactive = models.BooleanField(default=False)
    posted_at = models.DateTimeField(auto_now_add=True)

    @property
    def price(self):
        for items in self.item_set.all():
            total = 0.00
            total += float(items.price)
            return total

    def mark_inactive(self):
        if date.today == self.deadline:
            self.inactive = True
            if self.inactive:
                for item in self.item_set.all():
                    item.refund()
        return self.inactive

    def __str__(self):
        return self.title


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    description = models.TextField()
    image = models.URLField()
    list = models.ForeignKey(List)
    item_link = models.URLField()

    @property
    def reserved(self):
        total = self.pledge_set.aggregate(Sum('amount'))
        if len(self.pledge_set.all()) > 0:
            item_price = float(self.price)
            pledge_amount = float(total['amount__sum'])
            if item_price - pledge_amount == 0:
                return True
            elif item_price - pledge_amount < 0:
                refund_amount = -(item_price - pledge_amount)
                stripe.Refund.create(
                    charge=self.charge,
                    amount=refund_amount
                )
                return True
        return False

    def refund(self):
        if not self.reserved:
            for pledge in self.pledge_set.all():
                pledge.refund()

    def __str__(self):
        return self.name


class Pledge(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    charge = models.CharField(max_length=255, blank=False, null=True)
    pledge_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} donated'.format(self.user)

    def refund(self):
        stripe.api_key = STRIPE_API_KEY
        re = stripe.Refund.create(
            id=self.charge
        )
        return re
