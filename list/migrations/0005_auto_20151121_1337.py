# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_item_item_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='deadline',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='list',
            name='inactive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pledge',
            name='token',
            field=models.CharField(null=True, max_length=255),
        ),
    ]
