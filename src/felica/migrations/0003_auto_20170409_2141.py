# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('felica', '0002_auto_20170409_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='felicatime',
            name='master_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
