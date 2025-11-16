from django.db import models


class FAQ(models.Model):
    """Model for Frequently Asked Questions (সাধারণ জিজ্ঞাসা)"""
    
    STYLE_CHOICES = [
        ('faq-item-purple', 'Purple'),
        ('faq-item-blue', 'Blue'),
        ('faq-item-green', 'Green'),
        ('faq-item-orange', 'Orange'),
    ]
    
    # Question and Answer
    question = models.CharField(max_length=500, help_text="প্রশ্ন (e.g., রেজিস্ট্রেশন ফি কত?)")
    answer = models.TextField(help_text="উত্তর - HTML সমর্থিত")
    
    # Icon field - FontAwesome or Lucide icon
    icon_class = models.CharField(
        max_length=100,
        help_text="Icon class (e.g., fa-dollar-sign, dollar-sign for lucide)",
        default="help-circle"
    )
    
    # Styling
    style_class = models.CharField(
        max_length=50,
        help_text="FAQ item style class",
        default="faq-item-blue",
        choices=STYLE_CHOICES
    )
    
    # Additional features
    is_important = models.BooleanField(
        default=False,
        help_text="গুরুত্বপূর্ণ প্রশ্ন (will be shown first)"
    )
    is_expanded_by_default = models.BooleanField(
        default=False,
        help_text="ডিফল্টভাবে খোলা থাকবে"
    )
    
    # Ordering and status
    order = models.IntegerField(default=0, help_text="ক্রম নম্বর (কম নম্বর আগে দেখাবে)")
    is_active = models.BooleanField(default=True, help_text="সক্রিয় কিনা")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-is_important', 'order']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
    
    def __str__(self):
        return self.question
