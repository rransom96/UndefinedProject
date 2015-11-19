# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_pledge'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_link',
            field=models.URLField(default='http://www.amazon.com/PlayStation-4/dp/B00BGA9WK2/ref=lp_6427871011_1_7?s=videogames&ie=UTF8&qid=1447974737&sr=1-7'),
            preserve_default=False,
        ),
    ]
