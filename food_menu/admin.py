from django.contrib import admin
from .models import MealCategory, FoodItem


class FoodItemInline(admin.TabularInline):
    model = FoodItem
    extra = 1
    fields = ['name', 'quantity', 'description', 'icon_class', 'order', 'is_active']


@admin.register(MealCategory)
class MealCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'meal_type', 'icon_class', 'card_color_class', 'order', 'is_active']
    list_filter = ['meal_type', 'is_active']
    search_fields = ['name']
    list_editable = ['order', 'is_active']
    ordering = ['order']
    inlines = [FoodItemInline]
    
    fieldsets = (
        ('মূল তথ্য (Basic Info)', {
            'fields': ('name', 'meal_type')
        }),
        ('স্টাইলিং (Styling)', {
            'fields': ('icon_class', 'card_color_class')
        }),
        ('সেটিংস (Settings)', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity', 'description', 'order', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['category', 'order']
    
    fieldsets = (
        ('ক্যাটাগরি (Category)', {
            'fields': ('category',)
        }),
        ('খাবারের তথ্য (Food Details)', {
            'fields': ('name', 'quantity', 'description')
        }),
        ('স্টাইলিং (Styling)', {
            'fields': ('icon_class',)
        }),
        ('সেটিংস (Settings)', {
            'fields': ('order', 'is_active')
        }),
    )
