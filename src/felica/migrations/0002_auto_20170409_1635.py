# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('felica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='felicamember',
            name='master_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='felicamember',
            name='member_name',
            field=models.CharField(default=b'', max_length=200, null=True, verbose_name='member_name', blank=True),
        ),
    ]
