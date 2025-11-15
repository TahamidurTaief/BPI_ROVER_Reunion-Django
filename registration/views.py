from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration, Payment # Payment model import korun
from django.db import transaction # Database transaction er jonno

# --- Notun View ---
def register_page(request):
    """
    Dedicated registration page render kore.
    """
    return render(request, 'register_page.html')


# --- Oporibortito View ---
def landing_page(request):
    """
    Main landing page render kore.
    """
    return render(request, 'home.html')

# --- Oporibortito HTMX View ---
def htmx_get_step1_form(request):
    """
    Handles HTMX GET request for the first step of the form.
    """
    context = {
        'reg_types': Registration.REG_TYPE_CHOICES,
        'tshirt_sizes': Registration.TSHIRT_CHOICES,
        'scout_stages': Registration.SCOUT_STAGE_CHOICES,
    }
    return render(request, 'registration/partials/step1_form.html', context)

# --- Oporibortito HTMX View ---
def htmx_post_step1_form(request):
    """
    Handles HTMX POST from Step 1 without forms.py.
    Validates data, saves to session, and returns Step 2 form.
    """
    if request.method != 'POST':
        return HttpResponse(status=405)

    data = request.POST
    errors = {}
    
    # --- Manual Validation ---
    name = data.get('name')
    if not name:
        errors['name'] = 'আপনার নাম প্রয়োজন।'
        
    session = data.get('session')
    if not session:
        errors['session'] = 'আপনার সেশন প্রয়োজন।'
        
    contact_number = data.get('contact_number')
    if not contact_number:
        errors['contact_number'] = 'আপনার কন্টাক্ট নম্বর প্রয়োজন।'

    department = data.get('department')
    if not department:
        errors['department'] = 'আপনার ডিপার্টমেন্ট প্রয়োজন।'

    registration_type = data.get('registration_type')
    if not registration_type:
        errors['registration_type'] = 'রেজিস্ট্রেশনের ধরন সিলেক্ট করুন।'

    t_shirt_size = data.get('t_shirt_size')
    if not t_shirt_size:
        errors['t_shirt_size'] = 'টি-শার্ট সাইজ সিলেক্ট করুন।'
            
    last_scouting_stage = data.get('last_scouting_stage')
    if not last_scouting_stage:
        errors['last_scouting_stage'] = 'আপনার স্কাউটিং স্টেজ সিলেক্ট করুন।'

    if errors:
        # Data invalid, re-render step 1 with errors and old data
        context = {
            'errors': errors,
            'data': data, # To pre-fill the form
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
        'suggestion': data.get('suggestion', ''), # Optional field
    }
    
    # Render step 2
    context = {
        'payment_methods': Payment.PAYMENT_METHOD_CHOICES
    }
    return render(request, 'registration/partials/step2_payment.html', context)


# --- Oporibortito HTMX View ---
@transaction.atomic # Use transaction to ensure both objects are created
def htmx_post_step2_submit(request):
    """
    Handles HTMX POST from Step 2.
    Validates Step 2, retrieves Step 1 from session, creates Registration & Payment object.
    """
    if request.method != 'POST':
        return HttpResponse(status=405)
            
    step1_data = request.session.get('step1_data')
    
    # Payment fields
    payment_method = request.POST.get('payment_method')
    sender_number = request.POST.get('sender_number')
    trxn_id = request.POST.get('trxn_id')
    errors = {}
    context = {
        'payment_methods': Payment.PAYMENT_METHOD_CHOICES,
        'data': request.POST # Resend form data on error
    }

    if not step1_data:
        # Session expired. Send user back to start.
        errors['general'] = 'আপনার সেশন শেষ হয়েছে, দয়া করে আবার শুরু করুন।'
        context['errors'] = errors
        context['reg_types'] = Registration.REG_TYPE_CHOICES # Need to resend choices
        context['tshirt_sizes'] = Registration.TSHIRT_CHOICES
        context['scout_stages'] = Registration.SCOUT_STAGE_CHOICES
        return render(request, 'registration/partials/step1_form.html', context)

    # --- Manual Validation for Payment ---
    if not payment_method:
        errors['payment_method'] = 'পেমেন্ট মেথড সিলেক্ট করুন।'
    if not sender_number:
        errors['sender_number'] = 'আপনার পেমেন্ট নম্বরটি প্রয়োজন।'
    if not trxn_id:
        errors['trxn_id'] = 'আপনার ট্রানজেকশন আইডি প্রয়োজন।'
    
    # Check if Trxn ID already exists
    if trxn_id and Payment.objects.filter(trxn_id=trxn_id).exists():
        errors['trxn_id'] = 'এই ট্রানজেকশন আইডি ஏற்கனவே ব্যবহৃত হয়েছে।'

    if errors:
        context['errors'] = errors
        return render(request, 'registration/partials/step2_payment.html', context)
    
    # All good, create objects
    try:
        # Step 1: Create Registration object
        registration_obj = Registration.objects.create(**step1_data)
        
        # Step 2: Create Payment object linked to the registration
        Payment.objects.create(
            registration=registration_obj,
            payment_method=payment_method,
            sender_number=sender_number,
            trxn_id=trxn_id
        )
        
        # Clear session
        del request.session['step1_data']
        
        # Render success
        return render(request, 'registration/partials/step3_success.html')
        
    except Exception as e:
        # Database or other unexpected error
        errors['general'] = f"একটি ত্রুটি ঘটেছে: {e}"
        context['errors'] = errors
        return render(request, 'registration/partials/step2_payment.html', context)