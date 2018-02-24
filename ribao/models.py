# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models


class DailyRecord(models.Model):
    subject = models.CharField(verbose_name=u'项目名', max_length=20, default="")
    job_content = models.TextField(verbose_name=u'工作内容', max_length=100, default="")
    job_schedule = models.CharField(verbose_name=u'工作进度', max_length=20, default="", blank=True)
    job_plan = models.CharField(verbose_name=u"下周计划", max_length=100, default="", blank=True)
    name = models.CharField(verbose_name=u"接口人", max_length=100, default="", blank=True)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"日报详情"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.job_content