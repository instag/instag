# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('felica', '0003_auto_20170409_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='felicatime',
            name='work_end',
            field=models.DateTimeField(verbose_name='work_end'),
        ),
        migrations.AlterField(
            model_name='felicatime',
            name='work_start',
            field=models.DateTimeField(verbose_name='work_start'),
        ),
    ]
