from django.urls import path
from . import views

urlpatterns = [
    # Main landing page
    path('', views.landing_page, name='landing_page'),
    
    # Notun dedicated registration page
    path('register/', views.register_page, name='register_page'),
    
    # HTMX Endpoints (Eigulo oporibortito)
    path('htmx/get-step1-form/', views.htmx_get_step1_form, name='htmx_get_step1_form'),
    path('htmx/post-step1-form/', views.htmx_post_step1_form, name='htmx_post_step1_form'),
    path('htmx/post-step2-submit/', views.htmx_post_step2_submit, name='htmx_post_step2_submit'),
]