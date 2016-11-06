# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterCountJP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(default=b'', verbose_name='\ubcf8\ubb38')),
                ('body', models.TextField(default=b'', verbose_name='\ubcf8\ubb38')),
                ('profile_image_url', models.CharField(default=None, max_length=150, blank=True, null=True, verbose_name='url', db_index=True)),
                ('owner', models.CharField(default=None, max_length=50, null=True, verbose_name='url', blank=True)),
                ('uniqu_id', models.CharField(default=None, max_length=50, blank=True, null=True, verbose_name='owner_url', db_index=True)),
                ('rtCount', models.IntegerField(default=0, verbose_name='rtCount')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u4f5c\u6210\u65e5\u6642')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65e5\u6642')),
            ],
        ),
        migrations.CreateModel(
            name='TwitterCountKO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(default=b'', verbose_name='\ubcf8\ubb38')),
                ('body', models.TextField(default=b'', verbose_name='\ubcf8\ubb38')),
                ('profile_image_url', models.CharField(default=None, max_length=150, blank=True, null=True, verbose_name='url', db_index=True)),
                ('owner', models.CharField(default=None, max_length=50, null=True, verbose_name='url', blank=True)),
                ('uniqu_id', models.CharField(default=None, max_length=50, blank=True, null=True, verbose_name='owner_url', db_index=True)),
                ('rtCount', models.IntegerField(default=0, verbose_name='rtCount')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u4f5c\u6210\u65e5\u6642')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65e5\u6642')),
            ],
        ),
    ]
