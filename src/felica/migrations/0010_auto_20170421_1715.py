# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('felica', '0009_felicamember_hour_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='felicamember',
            name='felica_id',
            field=models.CharField(max_length=200, null=True, verbose_name='felica_id', blank=True),
        ),
        migrations.AlterField(
            model_name='felicatime',
            name='company_name',
            field=models.CharField(max_length=200, null=True, verbose_name='\ud68c\uc0ac\uba85', blank=True),
        ),
        migrations.AlterField(
            model_name='felicatime',
            name='member_name',
            field=models.CharField(max_length=200, null=True, verbose_name='\uc774\ub984', blank=True),
        ),
        migrations.AlterField(
            model_name='felicatime',
            name='work_end',
            field=models.DateTimeField(null=True, verbose_name='\ud1f4\uadfc'),
        ),
        migrations.AlterField(
            model_name='felicatime',
            name='work_start',
            field=models.DateTimeField(null=True, verbose_name='\ucd9c\uadfc'),
        ),
    ]
