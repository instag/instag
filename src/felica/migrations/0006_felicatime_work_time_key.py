# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('felica', '0005_auto_20170409_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='felicatime',
            name='work_time_key',
            field=models.CharField(max_length=100, null=True, verbose_name='work_time_key', blank=True),
        ),
    ]
