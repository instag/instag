# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_url', '0002_instagramplayermedia_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagramplayermedia',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 4, 15, 23, 16, 205784, tzinfo=utc), verbose_name='\u4f5c\u6210\u65e5\u6642', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instagramplayermedia',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 4, 15, 23, 19, 221747, tzinfo=utc), verbose_name='\u66f4\u65b0\u65e5\u6642', auto_now=True),
            preserve_default=False,
        ),
    ]
