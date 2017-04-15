# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('felica', '0006_felicatime_work_time_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='felicatime',
            name='work_time_total',
            field=models.IntegerField(null=True, verbose_name='work_time_total'),
        ),
    ]
