from django.db import models

class Registration(models.Model):
    # Choices
    REG_TYPE_CHOICES = [
        ('Ex Rover', 'Ex Rover'),
        ('Spouse/Guest', 'Spouse/Guest'),
        ('Children', 'Children'),
    ]
    
    TSHIRT_CHOICES = [
        ('XXL', 'XXL'),
        ('XL', 'XL'),
        ('L', 'L'),
        ('M', 'M'),
    ]
    
    SCOUT_STAGE_CHOICES = [
        ('Rover member', 'Rover member'),
        ('Rover Mate', 'Rover Mate'),
        ('Senior Rover Mate', 'Senior Rover Mate'),
    ]

    # Step 1 Fields
    name = models.CharField(max_length=255, verbose_name="Name")
    session = models.CharField(max_length=100, verbose_name="Session")
    contact_number = models.CharField(max_length=20, verbose_name="Contact Number")
    department = models.CharField(max_length=100, verbose_name="Department")
    registration_type = models.CharField(max_length=50, choices=REG_TYPE_CHOICES, verbose_name="Registration Type")
    t_shirt_size = models.CharField(max_length=10, choices=TSHIRT_CHOICES, verbose_name="T-Shirt Size")
    last_scouting_stage = models.CharField(max_length=50, choices=SCOUT_STAGE_CHOICES, verbose_name="Last Scouting Stage")
    suggestion = models.TextField(blank=True, null=True, verbose_name="Suggestion For Program If Any")
    
    # Utility fields
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.session}"

    class Meta:
        verbose_name = "Reunion Registration"
        verbose_name_plural = "Reunion Registrations"
        ordering = ['-created_at']


class Payment(models.Model):
    """
    Notun Payment Model
    """
    PAYMENT_METHOD_CHOICES = [
        ('Bkash', 'Bkash'),
        ('Nagad', 'Nagad'),
    ]

    # Registration model er sathe One-to-One link
    registration = models.OneToOneField(
        Registration, 
        on_delete=models.CASCADE, 
        related_name='payment',
        verbose_name="Registration"
    )
    
    # Transaction Way
    payment_method = models.CharField(
        max_length=20, 
        choices=PAYMENT_METHOD_CHOICES, 
        verbose_name="Payment Method"
    )
    
    # Transaction Number (Je number theke taka pathano hoyeche)
    sender_number = models.CharField(
        max_length=20, 
        verbose_name="Sender Number"
    )
    
    # Transaction ID
    trxn_id = models.CharField(
        max_length=255, 
        verbose_name="Transaction ID (Trxn ID)", 
        unique=True  # Ensure each Trxn ID is unique
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.registration.name} via {self.payment_method}"

    class Meta:
        verbose_name = "Payment Record"
        verbose_name_plural = "Payment Records"