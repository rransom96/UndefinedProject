# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_auto_20151121_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pledge',
            old_name='token',
            new_name='charge',
        ),
    ]
