# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('felica', '0002_auto_20170404_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='felicamember',
            name='felica_id',
            field=models.CharField(max_length=200, null=True, verbose_name='member_name', blank=True),
        ),
        migrations.AlterField(
            model_name='felicamember',
            name='member_name',
            field=models.CharField(max_length=200, null=True, verbose_name='member_name', blank=True),
        ),
    ]
