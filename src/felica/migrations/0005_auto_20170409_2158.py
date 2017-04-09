# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('felica', '0004_auto_20170409_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='felicatime',
            name='work_end',
            field=models.DateTimeField(null=True, verbose_name='work_end'),
        ),
        migrations.AlterField(
            model_name='felicatime',
            name='work_start',
            field=models.DateTimeField(null=True, verbose_name='work_start'),
        ),
    ]
