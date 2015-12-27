# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_url', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagramplayermedia',
            name='caption',
            field=models.TextField(default=b'', verbose_name='caption'),
        ),
    ]
