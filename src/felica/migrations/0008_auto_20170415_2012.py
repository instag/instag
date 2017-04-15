# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('felica', '0007_felicatime_work_time_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='felicatime',
            name='work_time_total',
        ),
        migrations.AddField(
            model_name='felicatime',
            name='work_time_hour',
            field=models.IntegerField(null=True, verbose_name='work_time_hour'),
        ),
        migrations.AddField(
            model_name='felicatime',
            name='work_time_minute',
            field=models.IntegerField(null=True, verbose_name='work_time_minute'),
        ),
    ]
