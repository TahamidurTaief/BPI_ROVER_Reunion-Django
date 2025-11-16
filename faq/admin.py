from django.contrib import admin
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'icon_class', 'style_class', 'is_important', 'is_expanded_by_default', 'order', 'is_active']
    list_filter = ['is_important', 'is_active', 'style_class', 'created_at']
    search_fields = ['question', 'answer']
    list_editable = ['order', 'is_active', 'is_important']
    ordering = ['-is_important', 'order']
    
    fieldsets = (
        ('প্রশ্ন ও উত্তর (Question & Answer)', {
            'fields': ('question', 'answer')
        }),
        ('স্টাইলিং (Styling)', {
            'fields': ('icon_class', 'style_class')
        }),
        ('বৈশিষ্ট্য (Features)', {
            'fields': ('is_important', 'is_expanded_by_default')
        }),
        ('সেটিংস (Settings)', {
            'fields': ('order', 'is_active')
        }),
    )
    
    date_hierarchy = 'created_at'
