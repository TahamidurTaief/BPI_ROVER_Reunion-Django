# New Apps Documentation - সময়সূচী, খাবার তালিকা, FAQ, শর্তাবলী

## Overview
Four new Django apps have been created to manage different sections of the Rover Reunion website:

1. **Schedule App** (সময়সূচী) - Event schedule management
2. **Food Menu App** (খাবার তালিকা) - Food menu management
3. **FAQ App** (সাধারণ জিজ্ঞাসা) - Frequently Asked Questions
4. **Terms App** (শর্তাবলী) - Terms and Conditions

---

## 1. Schedule App (সময়সূচী)

### Location
`/schedule/`

### Models

#### ScheduleItem
Manages individual schedule items for the event.

**Fields:**
- `start_time` (TimeField) - Event start time (e.g., 09:00)
- `end_time` (TimeField) - Event end time (e.g., 10:00)
- `title` (CharField) - Event title in Bengali
- `description` (TextField) - Detailed description
- `icon_class` (CharField) - FontAwesome/Lucide icon class (e.g., "coffee", "mic", "utensils", "gift")
- `color_class` (CharField) - Icon wrapper color class with choices:
  - `icon-wrapper-orange` - Orange gradient
  - `icon-wrapper-purple` - Purple gradient
  - `icon-wrapper-green` - Green gradient
  - `icon-wrapper-blue` - Blue gradient
- `order` (IntegerField) - Display order (lower numbers appear first)
- `is_active` (BooleanField) - Whether to display this item
- `created_at` (DateTimeField) - Auto timestamp
- `updated_at` (DateTimeField) - Auto timestamp

**Admin Features:**
- List view with time, title, icon, color, order, and status
- Inline editing for order and is_active
- Filterable by status and color
- Searchable by title and description
- Organized fieldsets in Bengali

**Management Command:**
```bash
python manage.py populate_schedule
```
Populates with 4 default schedule items from the home page.

---

## 2. Food Menu App (খাবার তালিকা)

### Location
`/food_menu/`

### Models

#### MealCategory
Manages meal categories (Breakfast, Lunch, Snacks).

**Fields:**
- `name` (CharField) - Category name in Bengali (e.g., "সকালের নাস্তা")
- `meal_type` (CharField) - Type with choices:
  - `breakfast` - সকালের নাস্তা (Breakfast)
  - `lunch` - দুপুরের খাবার (Lunch)
  - `snacks` - বিকালের নাস্তা (Snacks)
- `icon_class` (CharField) - Icon class (e.g., "coffee", "soup", "cup-soda")
- `card_color_class` (CharField) - Card styling with choices:
  - `food-card-breakfast` - Pink/Red gradient
  - `food-card-lunch` - Blue gradient
  - `food-card-snacks` - Green gradient
- `order` (IntegerField) - Display order
- `is_active` (BooleanField) - Whether to display
- Timestamps

#### FoodItem
Individual food items within meal categories.

**Fields:**
- `category` (ForeignKey) - Links to MealCategory
- `name` (CharField) - Food name in Bengali (e.g., "পরোটা")
- `description` (CharField) - Optional description (e.g., "গরম গরম", "তাজা")
- `quantity` (CharField) - Optional quantity (e.g., "২টি", "১ বোল")
- `icon_class` (CharField) - Icon class (default: "circle-dot")
- `order` (IntegerField) - Display order within category
- `is_active` (BooleanField) - Whether to display
- Timestamps

**Admin Features:**
- MealCategory admin with inline FoodItem editing
- Separate FoodItem admin for detailed management
- Filterable by category and status
- Searchable by name and description
- Organized fieldsets in Bengali

**Management Command:**
```bash
python manage.py populate_food_menu
```
Creates 3 meal categories and 13 food items from the home page.

---

## 3. FAQ App (সাধারণ জিজ্ঞাসা)

### Location
`/faq/`

### Models

#### FAQ
Manages Frequently Asked Questions.

**Fields:**
- `question` (CharField) - Question text in Bengali (up to 500 chars)
- `answer` (TextField) - Answer text (supports HTML)
- `icon_class` (CharField) - Icon class (e.g., "dollar-sign", "file-text", "users")
- `style_class` (CharField) - FAQ item styling with choices:
  - `faq-item-purple` - Purple theme
  - `faq-item-blue` - Blue theme
  - `faq-item-green` - Green theme
  - `faq-item-orange` - Orange theme
- `is_important` (BooleanField) - Important questions appear first
- `is_expanded_by_default` (BooleanField) - Whether to show expanded by default
- `order` (IntegerField) - Display order
- `is_active` (BooleanField) - Whether to display
- Timestamps

**Admin Features:**
- List view with question, icon, style, importance, and status
- Inline editing for order, status, and importance
- Filterable by importance, status, and style
- Searchable by question and answer
- Organized fieldsets in Bengali

**Management Command:**
```bash
python manage.py populate_faq
```
Creates 4 FAQ items from the home page with rich HTML answers.

---

## 4. Terms App (শর্তাবলী)

### Location
`/terms/`

### Models

#### TermsAndConditions
Manages Terms and Conditions items.

**Fields:**
- `title` (CharField) - Term title in Bengali (e.g., "অফেরতযোগ্য রেজিস্ট্রেশন")
- `description` (TextField) - Detailed description
- `icon_class` (CharField) - Icon class (e.g., "alert-triangle", "clock-alert", "ban")
- `icon_color_class` (CharField) - Icon color with choices:
  - `text-error` - Red (Error)
  - `text-warning` - Yellow (Warning)
  - `text-info` - Blue (Info)
  - `text-success` - Green (Success)
  - `text-accent` - Purple (Accent)
  - `text-primary` - Primary Color
- `is_critical` (BooleanField) - Critical terms appear first and highlighted
- `order` (IntegerField) - Display order
- `is_active` (BooleanField) - Whether to display
- Timestamps

**Admin Features:**
- List view with title, icon, color, criticality, and status
- Inline editing for order, status, and criticality
- Filterable by criticality, status, and color
- Searchable by title and description
- Organized fieldsets in Bengali

**Management Command:**
```bash
python manage.py populate_terms
```
Creates 6 terms items from the home page.

---

## Admin Panel Access

All apps are registered in the Django admin panel with Bengali verbose names:

1. **সময়সূচী (Schedule Management)** - `/admin/schedule/`
   - Schedule Items

2. **খাবার তালিকা (Food Menu Management)** - `/admin/food_menu/`
   - Meal Categories
   - Food Items

3. **সাধারণ জিজ্ঞাসা (FAQ Management)** - `/admin/faq/`
   - FAQs

4. **শর্তাবলী (Terms & Conditions Management)** - `/admin/terms/`
   - Terms and Conditions

## FontAwesome Icon Usage

All models support FontAwesome and Lucide icon classes. The admin will enter icon class names like:

**FontAwesome Examples:**
- `fa-coffee` or just `coffee`
- `fa-utensils` or just `utensils`
- `fa-microphone` or just `mic`
- `fa-dollar-sign` or just `dollar-sign`

**Lucide Icons (used in home page):**
- `coffee`
- `mic`
- `utensils`
- `gift`
- `dollar-sign`
- `file-text`
- `users`
- `credit-card`
- `alert-triangle`
- `clock-alert`
- `ban`
- `file-check`
- `backpack`
- `camera`

## Database Migrations

All migrations have been created and applied:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Initial Data Population

All apps come with management commands to populate initial data based on the home page content:

```bash
# Populate all data at once
python manage.py populate_schedule
python manage.py populate_food_menu
python manage.py populate_faq
python manage.py populate_terms
```

## Next Steps - Integration with Templates

To use these models in your templates, you'll need to:

1. **Create views** in each app to fetch the data
2. **Add context processors** or pass data in views
3. **Update templates** to use dynamic data instead of hardcoded content

### Example View Pattern:

```python
# schedule/views.py
from django.shortcuts import render
from .models import ScheduleItem

def schedule_list(request):
    schedules = ScheduleItem.objects.filter(is_active=True)
    return render(request, 'schedule/list.html', {'schedules': schedules})
```

### Example Template Usage:

```django
{% for item in schedules %}
<div class="timeline-card">
    <div class="icon-wrapper {{ item.color_class }}">
        <i data-lucide="{{ item.icon_class }}"></i>
    </div>
    <time>{{ item.start_time|time:"g:i A" }} - {{ item.end_time|time:"g:i A" }}</time>
    <h3>{{ item.title }}</h3>
    <p>{{ item.description }}</p>
</div>
{% endfor %}
```

## Testing

All models are working correctly:
- ✅ Schedule: 4 items created
- ✅ Food Menu: 3 categories, 13 items created
- ✅ FAQ: 4 items created
- ✅ Terms: 6 items created

You can now access the admin panel at `/admin/` to manage all content!

## Features Summary

### Schedule App
- ✅ Time-based event scheduling
- ✅ Dynamic icon and color selection
- ✅ Ordering system
- ✅ Active/inactive toggle

### Food Menu App
- ✅ Category-based organization
- ✅ Inline food item editing
- ✅ Quantity and description support
- ✅ Meal type classification

### FAQ App
- ✅ Rich HTML answer support
- ✅ Importance flagging
- ✅ Expandable by default option
- ✅ Style customization

### Terms App
- ✅ Criticality flagging
- ✅ Color-coded icons
- ✅ Detailed descriptions
- ✅ Flexible icon selection

---

## Troubleshooting

If you encounter any issues:

1. **Migration Issues:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Admin Not Showing:**
   - Check that all apps are in `INSTALLED_APPS`
   - Restart the development server

3. **Data Not Populating:**
   - Run the populate commands again
   - Check the database using Django shell:
     ```bash
     python manage.py shell
     >>> from schedule.models import ScheduleItem
     >>> ScheduleItem.objects.all()
     ```

## Contact

For any questions or issues, refer to the Django documentation or the project maintainer.
