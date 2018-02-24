# -*- coding: utf-8 -*-

import xadmin
from xadmin import views
from .models import DailyRecord


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "DevOps Daily 日报系统"
    site_footer = "DevOps Daily 日报系统 - by Chummy Liu"


class DailyRecordAdmin(object):
    list_display = ['subject', 'job_content', 'job_schedule', 'job_plan', 'name', 'add_time']
    search_fields = ['subject', 'job_content']
    list_filter = ['subject', 'job_content']


xadmin.site.register(DailyRecord, DailyRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)