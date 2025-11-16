from django.db import models


class ScheduleItem(models.Model):
    """Model for event schedule items (সময়সূচী)"""
    
    # Time fields
    start_time = models.TimeField(help_text="শুরুর সময় (e.g., 09:00)")
    end_time = models.TimeField(help_text="শেষ সময় (e.g., 10:00)")
    
    # Content fields
    title = models.CharField(max_length=200, help_text="শিরোনাম (e.g., রিপোর্টিং ও সকালের নাস্তা)")
    description = models.TextField(help_text="বিস্তারিত বর্ণনা")
    
    # Icon field - Lucide icon name
    icon_class = models.CharField(
        max_length=100,
        help_text="Lucide icon name (e.g., coffee, utensils, mic, gift, calendar)",
        default="calendar"
    )
    
    # Additional styling
    color_class = models.CharField(
        max_length=50,
        help_text="Color wrapper class (e.g., icon-wrapper-orange, icon-wrapper-purple)",
        default="icon-wrapper-blue",
        choices=[
            ('icon-wrapper-orange', 'Orange'),
            ('icon-wrapper-purple', 'Purple'),
            ('icon-wrapper-green', 'Green'),
            ('icon-wrapper-blue', 'Blue'),
        ]
    )
    
    # Ordering and status
    order = models.IntegerField(default=0, help_text="ক্রম নম্বর (কম নম্বর আগে দেখাবে)")
    is_active = models.BooleanField(default=True, help_text="সক্রিয় কিনা")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'start_time']
        verbose_name = "Schedule Item"
        verbose_name_plural = "Schedule Items"
    
    def __str__(self):
        return f"{self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')} | {self.title}"
    
    def get_time_display(self):
        """Return formatted time in Bengali style"""
        return f"সকাল {self.start_time.strftime('%I:%M')} - {self.end_time.strftime('%I:%M')}"
