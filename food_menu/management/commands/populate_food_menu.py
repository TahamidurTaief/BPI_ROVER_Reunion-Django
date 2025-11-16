from django.core.management.base import BaseCommand
from food_menu.models import MealCategory, FoodItem


class Command(BaseCommand):
    help = 'Populate food menu with initial data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        FoodItem.objects.all().delete()
        MealCategory.objects.all().delete()
        
        # Create Breakfast Category
        breakfast = MealCategory.objects.create(
            name='সকালের নাস্তা',
            meal_type='breakfast',
            icon_class='coffee',
            card_color_class='food-card-breakfast',
            order=1
        )
        
        breakfast_items = [
            {'name': 'পরোটা', 'quantity': '২টি', 'description': 'গরম গরম', 'order': 1},
            {'name': 'সবজি ভাজি', 'description': 'তাজা', 'order': 2},
            {'name': 'ডিম ওমলেট', 'description': 'স্পেশাল', 'order': 3},
            {'name': 'মিনারেল ওয়াটার', 'order': 4},
        ]
        
        for item_data in breakfast_items:
            FoodItem.objects.create(category=breakfast, **item_data)
            self.stdout.write(self.style.SUCCESS(f'Created breakfast item: {item_data["name"]}'))
        
        # Create Lunch Category
        lunch = MealCategory.objects.create(
            name='দুপুরের খাবার',
            meal_type='lunch',
            icon_class='soup',
            card_color_class='food-card-lunch',
            order=2
        )
        
        lunch_items = [
            {'name': 'কাচ্চি বিরিয়ানি', 'description': 'বাসমতি', 'order': 1},
            {'name': 'চিকেন রোস্ট', 'description': 'জুসি', 'order': 2},
            {'name': 'কাবাব', 'description': 'স্পাইসি', 'order': 3},
            {'name': 'বোরহানি', 'description': 'ঠান্ডা', 'order': 4},
            {'name': 'মিষ্টি', 'description': 'মুখ মিষ্টি করার জন্য', 'order': 5},
        ]
        
        for item_data in lunch_items:
            FoodItem.objects.create(category=lunch, **item_data)
            self.stdout.write(self.style.SUCCESS(f'Created lunch item: {item_data["name"]}'))
        
        # Create Snacks Category
        snacks = MealCategory.objects.create(
            name='বিকালের নাস্তা',
            meal_type='snacks',
            icon_class='cup-soda',
            card_color_class='food-card-snacks',
            order=3
        )
        
        snacks_items = [
            {'name': 'সিঙ্গারা / সমুচা', 'description': 'কুরকুরে', 'order': 1},
            {'name': 'চা / কফি', 'description': 'গরম', 'order': 2},
            {'name': 'বিস্কুট', 'description': 'মচমচে', 'order': 3},
            {'name': 'চকলেট', 'description': 'মিষ্টি', 'order': 4},
        ]
        
        for item_data in snacks_items:
            FoodItem.objects.create(category=snacks, **item_data)
            self.stdout.write(self.style.SUCCESS(f'Created snacks item: {item_data["name"]}'))
        
        self.stdout.write(self.style.SUCCESS('Successfully populated food menu'))
