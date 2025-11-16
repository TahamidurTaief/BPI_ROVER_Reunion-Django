from django.db import models


class TermsAndConditions(models.Model):
    """Model for Terms and Conditions (শর্তাবলী)"""
    
    ICON_COLOR_CHOICES = [
        ('text-error', 'Red (Error)'),
        ('text-warning', 'Yellow (Warning)'),
        ('text-info', 'Blue (Info)'),
        ('text-success', 'Green (Success)'),
        ('text-accent', 'Purple (Accent)'),
        ('text-primary', 'Primary Color'),
    ]
    
    # Title and description
    title = models.CharField(
        max_length=200,
        help_text="শিরোনাম (e.g., অফেরতযোগ্য রেজিস্ট্রেশন)"
    )
    description = models.TextField(
        help_text="বিস্তারিত বর্ণনা"
    )
    
    # Icon field - FontAwesome or Lucide icon
    icon_class = models.CharField(
        max_length=100,
        help_text="Icon class (e.g., fa-alert-triangle, alert-triangle for lucide)",
        default="alert-triangle"
    )
    
    # Icon color
    icon_color_class = models.CharField(
        max_length=50,
        help_text="Icon color class",
        default="text-error",
        choices=ICON_COLOR_CHOICES
    )
    
    # Features
    is_critical = models.BooleanField(
        default=False,
        help_text="গুরুত্বপূর্ণ শর্ত (will be highlighted)"
    )
    
    # Ordering and status
    order = models.IntegerField(default=0, help_text="ক্রম নম্বর (কম নম্বর আগে দেখাবে)")
    is_active = models.BooleanField(default=True, help_text="সক্রিয় কিনা")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-is_critical', 'order']
        verbose_name = "Terms and Conditions"
        verbose_name_plural = "Terms and Conditions"
    
    def __str__(self):
        return self.title
