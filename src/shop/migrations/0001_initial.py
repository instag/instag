# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_url', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shop_title', models.CharField(max_length=200, null=True, verbose_name='SHOP \uc774\ub984', blank=True)),
                ('shop_description', models.TextField(default=b'', verbose_name='SHOP \uc18c\uac1c')),
                ('user', models.ForeignKey(to='instagram_url.InstagramPlayer')),
            ],
        ),
    ]
