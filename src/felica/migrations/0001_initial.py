# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FelicaMember',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('company_name', models.CharField(max_length=200, null=True, verbose_name='\u4f1a\u793e\u540d', blank=True)),
                ('member_name', models.CharField(max_length=200, null=True, verbose_name='member_name', blank=True)),
                ('felica_id', models.CharField(max_length=200, null=True, verbose_name='member_name', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u4f5c\u6210\u65e5\u6642')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65e5\u6642')),
                ('master_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FelicaTime',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('company_name', models.CharField(max_length=200, null=True, verbose_name='\u4f1a\u793e\u540d', blank=True)),
                ('member_name', models.CharField(max_length=200, null=True, verbose_name='\u4f1a\u793e\u540d', blank=True)),
                ('work_start', models.DateTimeField(auto_now_add=True, verbose_name='work_start')),
                ('work_end', models.DateTimeField(auto_now_add=True, verbose_name='work_end')),
                ('felica_id', models.CharField(max_length=200, null=True, verbose_name='felica_id', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u4f5c\u6210\u65e5\u6642')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65e5\u6642')),
                ('master_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
