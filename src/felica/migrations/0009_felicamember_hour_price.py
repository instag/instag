# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('felica', '0008_auto_20170415_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='felicamember',
            name='hour_price',
            field=models.IntegerField(null=True, verbose_name='hour_price'),
        ),
    ]
