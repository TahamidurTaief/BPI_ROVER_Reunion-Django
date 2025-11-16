from django.contrib import admin
from .models import ScheduleItem


@admin.register(ScheduleItem)
class ScheduleItemAdmin(admin.ModelAdmin):
    list_display = ['start_time', 'end_time', 'title', 'icon_class', 'color_class', 'order', 'is_active']
    list_filter = ['is_active', 'color_class', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'start_time']
    
    fieldsets = (
        ('সময় (Time)', {
            'fields': ('start_time', 'end_time')
        }),
        ('বিষয়বস্তু (Content)', {
            'fields': ('title', 'description')
        }),
        ('স্টাইলিং (Styling)', {
            'fields': ('icon_class', 'color_class')
        }),
        ('সেটিংস (Settings)', {
            'fields': ('order', 'is_active')
        }),
    )
    
    date_hierarchy = 'created_at'
