# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_token', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('user_id', models.IntegerField()),
                ('full_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('media_id', models.CharField(max_length=255)),
                ('allowed', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Media',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=255)),
                ('tag_flg', models.IntegerField(default=0, verbose_name='tag_flg', db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\uc791\uc131 \uc77c\uc790')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='\uac31\uc2e0 \uc77c\uc790')),
            ],
        ),
    ]
