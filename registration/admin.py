from django.contrib import admin
from .models import Registration, Payment
from import_export.admin import ImportExportModelAdmin

class PaymentInline(admin.TabularInline):
    """
    Allows editing Payment details directly within the Registration admin page.
    """
    model = Payment
    can_delete = False
    verbose_name_plural = 'Payment Details'
    extra = 0 # Don't show extra blank forms
    fields = ('payment_method', 'sender_number', 'trxn_id', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(Registration)
class RegistrationAdmin(ImportExportModelAdmin):
    """
    Admin configuration for Reunion Registrations.
    """
    
    list_display = (
        'name', 
        'session', 
        'contact_number', 
        'department', 
        'registration_type', 
        'has_payment', # Custom method to check payment
        'created_at'
    )
    
    list_filter = (
        'session', 
        'department', 
        'registration_type', 
        't_shirt_size', 
        'last_scouting_stage'
    )
    
    search_fields = (
        'name', 
        'session', 
        'contact_number', 
        'department', 
        'payment__trxn_id' # Search by Trxn ID
    )
    
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'session', 'contact_number', 'department', 'suggestion')
        }),
        ('Registration Details', {
            'fields': ('registration_type', 't_shirt_size', 'last_scouting_stage')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )
    
    # Add the Payment inline to the admin
    inlines = [PaymentInline]
    
    resource_class = None 
    
    @admin.display(boolean=True, description='Payment Done?')
    def has_payment(self, obj):
        return hasattr(obj, 'payment')

# Ekhon ar alada Payment admin register korar dorkar nei,
# Kintu korle o shomossha nei.
# @admin.register(Payment)
# class PaymentAdmin(admin.ModelAdmin):
#     list_display = ('registration', 'payment_method', 'sender_number', 'trxn_id', 'created_at')
#     search_fields = ('registration__name', 'sender_number', 'trxn_id')