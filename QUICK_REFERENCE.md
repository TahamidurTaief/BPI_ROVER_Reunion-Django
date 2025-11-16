# Quick Reference - New Apps

## All Management Commands

```bash
# Populate all data (run these commands in order)
python manage.py populate_schedule
python manage.py populate_food_menu
python manage.py populate_faq
python manage.py populate_terms
```

## Admin URLs

- Schedule: http://localhost:8000/admin/schedule/scheduleitem/
- Food Menu Categories: http://localhost:8000/admin/food_menu/mealcategory/
- Food Items: http://localhost:8000/admin/food_menu/fooditem/
- FAQs: http://localhost:8000/admin/faq/faq/
- Terms: http://localhost:8000/admin/terms/termsandconditions/

## Model Quick Reference

### Schedule (সময়সূচী)
```python
from schedule.models import ScheduleItem

# Get all active schedules
schedules = ScheduleItem.objects.filter(is_active=True)

# Get by order
schedules = ScheduleItem.objects.filter(is_active=True).order_by('order')
```

### Food Menu (খাবার তালিকা)
```python
from food_menu.models import MealCategory, FoodItem

# Get all categories with their items
categories = MealCategory.objects.filter(is_active=True).prefetch_related('food_items')

# Get breakfast items
breakfast = MealCategory.objects.get(meal_type='breakfast')
breakfast_items = breakfast.food_items.filter(is_active=True)
```

### FAQ (সাধারণ জিজ্ঞাসা)
```python
from faq.models import FAQ

# Get all active FAQs
faqs = FAQ.objects.filter(is_active=True)

# Get important FAQs first
faqs = FAQ.objects.filter(is_active=True).order_by('-is_important', 'order')
```

### Terms (শর্তাবলী)
```python
from terms.models import TermsAndConditions

# Get all active terms
terms = TermsAndConditions.objects.filter(is_active=True)

# Get critical terms first
terms = TermsAndConditions.objects.filter(is_active=True).order_by('-is_critical', 'order')
```

## Common Icon Classes

### Lucide Icons (used in templates)
- `calendar-days` - Calendar
- `calendar-check` - Calendar with check
- `clock` - Clock
- `map-pin` - Location pin
- `coffee` - Coffee cup
- `mic` - Microphone
- `utensils` - Fork and knife
- `gift` - Gift box
- `utensils-crossed` - Crossed utensils
- `soup` - Soup bowl
- `cup-soda` - Beverage cup
- `help-circle` - Help icon
- `dollar-sign` - Money
- `file-text` - Document
- `users` - Multiple users
- `credit-card` - Credit card
- `alert-triangle` - Warning triangle
- `clock-alert` - Clock with alert
- `ban` - Ban/prohibited
- `file-check` - Document with check
- `backpack` - Backpack
- `camera` - Camera
- `circle-dot` - Bullet point

## Color Classes

### Schedule Icon Wrappers
- `icon-wrapper-orange` - Orange gradient
- `icon-wrapper-purple` - Purple gradient
- `icon-wrapper-green` - Green gradient
- `icon-wrapper-blue` - Blue gradient

### Food Card Colors
- `food-card-breakfast` - Pink/Red gradient
- `food-card-lunch` - Blue gradient
- `food-card-snacks` - Green gradient

### FAQ Styles
- `faq-item-purple` - Purple theme
- `faq-item-blue` - Blue theme
- `faq-item-green` - Green theme
- `faq-item-orange` - Orange theme

### Terms Icon Colors
- `text-error` - Red
- `text-warning` - Yellow
- `text-info` - Blue
- `text-success` - Green
- `text-accent` - Purple
- `text-primary` - Primary color

## Database Stats

After running populate commands:
- ✅ Schedule Items: 4
- ✅ Meal Categories: 3
- ✅ Food Items: 13
- ✅ FAQs: 4
- ✅ Terms: 6

Total: **30 database records** created!

## Development Server

```bash
# Start server
python manage.py runserver

# Access admin
http://localhost:8000/admin/

# Homepage
http://localhost:8000/
```

## Check Everything is Working

```bash
# Django shell
python manage.py shell

# Then in shell:
from schedule.models import ScheduleItem
from food_menu.models import MealCategory, FoodItem
from faq.models import FAQ
from terms.models import TermsAndConditions

print(f"Schedules: {ScheduleItem.objects.count()}")
print(f"Meal Categories: {MealCategory.objects.count()}")
print(f"Food Items: {FoodItem.objects.count()}")
print(f"FAQs: {FAQ.objects.count()}")
print(f"Terms: {TermsAndConditions.objects.count()}")
```

Expected output:
```
Schedules: 4
Meal Categories: 3
Food Items: 13
FAQs: 4
Terms: 6
```
