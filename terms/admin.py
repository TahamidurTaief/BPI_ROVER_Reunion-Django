from django.contrib import admin
from .models import TermsAndConditions


@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_class', 'icon_color_class', 'is_critical', 'order', 'is_active']
    list_filter = ['is_critical', 'is_active', 'icon_color_class', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active', 'is_critical']
    ordering = ['-is_critical', 'order']
    
    fieldsets = (
        ('শিরোনাম ও বর্ণনা (Title & Description)', {
            'fields': ('title', 'description')
        }),
        ('স্টাইলিং (Styling)', {
            'fields': ('icon_class', 'icon_color_class')
        }),
        ('বৈশিষ্ট্য (Features)', {
            'fields': ('is_critical',)
        }),
        ('সেটিংস (Settings)', {
            'fields': ('order', 'is_active')
        }),
    )
    
    date_hierarchy = 'created_at'
