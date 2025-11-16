from django.shortcuts import render
from schedule.models import ScheduleItem
from food_menu.models import MealCategory, FoodItem
from faq.models import FAQ
from terms.models import TermsAndConditions


def home(request):
    """
    Home page with dynamic content from database
    """
    # Fetch all active data ordered appropriately
    schedules = ScheduleItem.objects.filter(is_active=True).order_by('order', 'start_time')
    meal_categories = MealCategory.objects.filter(is_active=True).prefetch_related('food_items').order_by('order')
    faqs = FAQ.objects.filter(is_active=True).order_by('-is_important', 'order')
    terms = TermsAndConditions.objects.filter(is_active=True).order_by('-is_critical', 'order')
    
    context = {
        'schedules': schedules,
        'meal_categories': meal_categories,
        'faqs': faqs,
        'terms': terms,
    }
    
    return render(request, 'home.html', context)