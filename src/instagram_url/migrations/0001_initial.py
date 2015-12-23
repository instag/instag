# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramPlayer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0, verbose_name='uer_id', db_index=True)),
                ('user_name', models.CharField(default=b'', max_length=100, verbose_name='user_name')),
                ('user_site_id', models.IntegerField(default=0, verbose_name='uer_id')),
                ('code', models.TextField(default=b'', verbose_name='code')),
                ('media_cnt', models.IntegerField(default=0, verbose_name='media_cnt', db_index=True)),
                ('followed_by', models.IntegerField(default=0, verbose_name='followed_by', db_index=True)),
                ('follows', models.IntegerField(default=0, verbose_name='follows', db_index=True)),
                ('tag_1', models.CharField(default=b'', max_length=100, verbose_name='tag_1')),
                ('tag_2', models.CharField(default=b'', max_length=100, verbose_name='tag_2')),
                ('tag_3', models.CharField(default=b'', max_length=100, verbose_name='tag_3')),
                ('tag_4', models.CharField(default=b'', max_length=100, verbose_name='tag_4')),
                ('tag_5', models.CharField(default=b'', max_length=100, verbose_name='tag_5')),
                ('tag_6', models.CharField(default=b'', max_length=100, verbose_name='tag_6')),
                ('follow_total', models.IntegerField(default=0, verbose_name='follow_total', db_index=True)),
                ('like_total', models.IntegerField(default=0, verbose_name='like_total', db_index=True)),
                ('point', models.IntegerField(default=100, verbose_name='point', db_index=True)),
                ('oauth_token', models.TextField(default=b'', verbose_name='oauth_token')),
                ('profile_picture', models.TextField(default=b'', verbose_name='profile_picture')),
                ('relation_flg', models.IntegerField(default=0, verbose_name='relation_flg', db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u4f5c\u6210\u65e5\u6642')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65e5\u6642')),
            ],
        ),
        migrations.CreateModel(
            name='InstagramPlayerFollowHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0, verbose_name='uer_id', db_index=True)),
                ('target_id', models.IntegerField(default=0, verbose_name='target_id', db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u4f5c\u6210\u65e5\u6642')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65e5\u6642')),
            ],
        ),
        migrations.CreateModel(
            name='InstagramPlayerMedia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('media_id', models.CharField(default=b'', max_length=100, verbose_name='media_id')),
                ('low_resolution_url', models.TextField(default=b'', verbose_name='low_resolution_url')),
                ('standard_resolution_url', models.TextField(default=b'', verbose_name='standard_resolution_url')),
                ('thumbnail_url', models.TextField(default=b'', verbose_name='_thumbnail_url')),
                ('media_link', models.CharField(default=b'', max_length=100, verbose_name='link')),
                ('tags', models.TextField(default=b'', verbose_name='tags')),
                ('media_type', models.CharField(default=b'', max_length=100, verbose_name='media_type')),
                ('user', models.ForeignKey(to='instagram_url.InstagramPlayer')),
            ],
        ),
    ]
