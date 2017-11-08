# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-11-08 04:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2017, 11, 8, 4, 32, 38, 790828, tzinfo=utc))),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
