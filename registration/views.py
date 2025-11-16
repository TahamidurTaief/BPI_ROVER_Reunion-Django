from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration, Payment
from django.db import transaction
from django.views.decorators.http import require_http_methods
from .models import Registration, Payment # Payment model import korun
from django.db import transaction # Database transaction er jonno
from schedule.models import ScheduleItem
from food_menu.models import MealCategory, FoodItem
from faq.models import FAQ
from terms.models import TermsAndConditions


# --- Notun View ---
def register_page(request):
    """
    Dedicated registration page render kore.
    """
    return render(request, 'register_page.html')


# --- Main Landing Page ---
def landing_page(request):
    """
    Main landing page render kore with dynamic content from database.
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

# --- HTMX Step 1: Get Initial Form ---
@require_http_methods(["GET"])
def htmx_get_step1_form(request):
    """
    Handles HTMX GET request for the first step of the form.
    Returns the initial registration form.
    """
    context = {
        'reg_types': Registration.REG_TYPE_CHOICES,
        'tshirt_sizes': Registration.TSHIRT_CHOICES,
        'scout_stages': Registration.SCOUT_STAGE_CHOICES,
    }
    return render(request, 'registration/partials/step1_form.html', context)


# --- HTMX Step 1: Submit Personal Info ---
@require_http_methods(["POST"])
def htmx_post_step1_form(request):
    """
    Handles HTMX POST from Step 1.
    Validates data, saves to session, and returns Step 2 payment form.
    """
    data = request.POST
    errors = {}
    
    # --- Manual Validation ---
    name = data.get('name', '').strip()
    if not name:
        errors['name'] = 'আপনার নাম প্রয়োজন।'
        
    session = data.get('session', '').strip()
    if not session:
        errors['session'] = 'আপনার সেশন প্রয়োজন।'
        
    contact_number = data.get('contact_number', '').strip()
    if not contact_number:
        errors['contact_number'] = 'আপনার কন্টাক্ট নম্বর প্রয়োজন।'
    elif len(contact_number) < 11 or not contact_number.replace('+', '').replace('-', '').isdigit():
        errors['contact_number'] = 'সঠিক মোবাইল নম্বর দিন (যেমন: 01712345678)।'

    department = data.get('department', '').strip()
    if not department:
        errors['department'] = 'আপনার ডিপার্টমেন্ট প্রয়োজন।'

    registration_type = data.get('registration_type', '').strip()
    if not registration_type:
        errors['registration_type'] = 'রেজিস্ট্রেশনের ধরন সিলেক্ট করুন।'

    t_shirt_size = data.get('t_shirt_size', '').strip()
    if not t_shirt_size:
        errors['t_shirt_size'] = 'টি-শার্ট সাইজ সিলেক্ট করুন।'
            
    last_scouting_stage = data.get('last_scouting_stage', '').strip()
    if not last_scouting_stage:
        errors['last_scouting_stage'] = 'আপনার স্কাউটিং স্টেজ সিলেক্ট করুন।'

    if errors:
        # Data invalid, re-render step 1 with errors and old data
        context = {
            'errors': errors,
            'data': data,
            'reg_types': Registration.REG_TYPE_CHOICES,
            'tshirt_sizes': Registration.TSHIRT_CHOICES,
            'scout_stages': Registration.SCOUT_STAGE_CHOICES,
        }
        return render(request, 'registration/partials/step1_form.html', context)

    # No errors, save clean data to session
    request.session['step1_data'] = {
        'name': name,
        'session': session,
        'contact_number': contact_number,
        'department': department,
        'registration_type': registration_type,
        't_shirt_size': t_shirt_size,
        'last_scouting_stage': last_scouting_stage,
        'suggestion': data.get('suggestion', '').strip(),
    }
    
    # Render step 2 payment form
    context = {
        'payment_methods': Payment.PAYMENT_METHOD_CHOICES
    }
    return render(request, 'registration/partials/step2_payment.html', context)


# --- HTMX Step 2: Submit Payment & Complete Registration ---
@transaction.atomic
@require_http_methods(["POST"])
def htmx_post_step2_submit(request):
    """
    Handles HTMX POST from Step 2.
    Validates payment info, retrieves Step 1 data from session,
    creates Registration & Payment objects, and shows success page.
    """
    step1_data = request.session.get('step1_data')
    
    # Payment fields
    payment_method = request.POST.get('payment_method', '').strip()
    sender_number = request.POST.get('sender_number', '').strip()
    trxn_id = request.POST.get('trxn_id', '').strip()
    
    errors = {}
    context = {
        'payment_methods': Payment.PAYMENT_METHOD_CHOICES,
        'data': request.POST
    }

    if not step1_data:
        # Session expired, send user back to start
        errors['general'] = 'আপনার সেশন শেষ হয়েছে, দয়া করে আবার শুরু করুন।'
        context['errors'] = errors
        context['reg_types'] = Registration.REG_TYPE_CHOICES
        context['tshirt_sizes'] = Registration.TSHIRT_CHOICES
        context['scout_stages'] = Registration.SCOUT_STAGE_CHOICES
        return render(request, 'registration/partials/step1_form.html', context)

    # --- Manual Validation for Payment ---
    if not payment_method:
        errors['payment_method'] = 'পেমেন্ট মেথড সিলেক্ট করুন।'
    
    if not sender_number:
        errors['sender_number'] = 'আপনার পেমেন্ট নম্বরটি প্রয়োজন।'
    elif len(sender_number) < 11 or not sender_number.replace('+', '').replace('-', '').isdigit():
        errors['sender_number'] = 'সঠিক মোবাইল নম্বর দিন (যেমন: 01712345678)।'
    
    if not trxn_id:
        errors['trxn_id'] = 'আপনার ট্রানজেকশন আইডি প্রয়োজন।'
    elif len(trxn_id) < 5:
        errors['trxn_id'] = 'সঠিক ট্রানজেকশন আইডি দিন।'
    elif Payment.objects.filter(trxn_id=trxn_id).exists():
        errors['trxn_id'] = 'এই ট্রানজেকশন আইডি ইতিমধ্যে ব্যবহৃত হয়েছে।'

    if errors:
        context['errors'] = errors
        return render(request, 'registration/partials/step2_payment.html', context)
    
    # All validation passed, create database records
    try:
        # Step 1: Create Registration object
        registration_obj = Registration.objects.create(**step1_data)
        
        # Step 2: Create Payment object linked to registration
        Payment.objects.create(
            registration=registration_obj,
            payment_method=payment_method,
            sender_number=sender_number,
            trxn_id=trxn_id
        )
        
        # Clear session data
        if 'step1_data' in request.session:
            del request.session['step1_data']
        
        # Render success page
        return render(request, 'registration/partials/step3_success.html')
        
    except Exception as e:
        # Database or other unexpected error
        errors['general'] = f"একটি ত্রুটি ঘটেছে: {str(e)}"
        context['errors'] = errors
        return render(request, 'registration/partials/step2_payment.html', context)