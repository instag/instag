# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_url', '0003_auto_20160105_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagramplayermedia',
            name='comment_count',
            field=models.CharField(default=b'', max_length=100, verbose_name='comment_count'),
        ),
        migrations.AddField(
            model_name='instagramplayermedia',
            name='like_count',
            field=models.CharField(default=b'', max_length=100, verbose_name='like_count'),
        ),
    ]
