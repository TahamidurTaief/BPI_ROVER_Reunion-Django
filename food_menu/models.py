from django.db import models


class MealCategory(models.Model):
    """Model for meal categories (খাবার তালিকা categories)"""
    
    MEAL_TYPE_CHOICES = [
        ('breakfast', 'সকালের নাস্তা (Breakfast)'),
        ('lunch', 'দুপুরের খাবার (Lunch)'),
        ('snacks', 'বিকালের নাস্তা (Snacks)'),
    ]
    
    # Basic fields
    name = models.CharField(max_length=100, help_text="ক্যাটাগরির নাম (e.g., সকালের নাস্তা)")
    meal_type = models.CharField(
        max_length=20, 
        choices=MEAL_TYPE_CHOICES,
        unique=True,
        help_text="খাবারের ধরন"
    )
    
    # Icon field - FontAwesome or Lucide icon
    icon_class = models.CharField(
        max_length=100,
        help_text="Icon class (e.g., fa-coffee, coffee for lucide)",
        default="utensils"
    )
    
    # Styling
    card_color_class = models.CharField(
        max_length=50,
        help_text="Card color class (e.g., food-card-breakfast, food-card-lunch)",
        default="food-card",
        choices=[
            ('food-card-breakfast', 'Breakfast (Pink/Red)'),
            ('food-card-lunch', 'Lunch (Blue)'),
            ('food-card-snacks', 'Snacks (Green)'),
        ]
    )
    
    # Ordering and status
    order = models.IntegerField(default=0, help_text="ক্রম নম্বর")
    is_active = models.BooleanField(default=True, help_text="সক্রিয় কিনা")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Meal Category"
        verbose_name_plural = "Meal Categories"
    
    def __str__(self):
        return self.name


class FoodItem(models.Model):
    """Model for individual food items within meal categories"""
    
    # Foreign key to category
    category = models.ForeignKey(
        MealCategory,
        on_delete=models.CASCADE,
        related_name='food_items',
        help_text="খাবারের ক্যাটাগরি"
    )
    
    # Food details
    name = models.CharField(max_length=200, help_text="খাবারের নাম (e.g., পরোটা)")
    description = models.CharField(
        max_length=100,
        blank=True,
        help_text="অতিরিক্ত বিবরণ (e.g., গরম গরম, তাজা)"
    )
    quantity = models.CharField(
        max_length=50,
        blank=True,
        help_text="পরিমাণ (e.g., ২টি, ১ বোল)"
    )
    
    # Icon for list item (optional)
    icon_class = models.CharField(
        max_length=100,
        help_text="Icon class (e.g., circle-dot)",
        default="circle-dot"
    )
    
    # Ordering and status
    order = models.IntegerField(default=0, help_text="ক্রম নম্বর")
    is_active = models.BooleanField(default=True, help_text="সক্রিয় কিনা")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['category', 'order']
        verbose_name = "Food Item"
        verbose_name_plural = "Food Items"
    
    def __str__(self):
        display_text = self.name
        if self.quantity:
            display_text += f" ({self.quantity})"
        if self.description:
            display_text += f" - {self.description}"
        return display_text
