from atexit import register
from django.contrib import admin

from .models import Resourse


class ResourseAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'ip_address',
        'port',
        'resourse_type',
        'host_user',
    )
    list_editable = ('ip_address', 'port', 'resourse_type', 'host_user')
    search_fields = ('ip_address', 'host_user')
    list_filter = ('change_datetime',)
    empty_value_display = '-empty-'

admin.site.register(Resourse, ResourseAdmin)
