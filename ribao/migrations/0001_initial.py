# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-18 11:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='', max_length=20, verbose_name='\u9879\u76ee\u540d')),
                ('job_content', models.CharField(default='', max_length=100, verbose_name='\u5de5\u4f5c\u5185\u5bb9')),
                ('job_schedule', models.CharField(blank=True, default='', max_length=20, verbose_name='\u5de5\u4f5c\u8fdb\u5ea6')),
                ('job_plan', models.CharField(blank=True, default='', max_length=100, verbose_name='\u4e0b\u5468\u8ba1\u5212')),
                ('name', models.CharField(blank=True, default='', max_length=100, verbose_name='\u63a5\u53e3\u4eba')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u65e5\u62a5\u8be6\u60c5',
                'verbose_name_plural': '\u65e5\u62a5\u8be6\u60c5',
            },
        ),
    ]
