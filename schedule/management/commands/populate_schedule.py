from django.core.management.base import BaseCommand
from schedule.models import ScheduleItem
from datetime import time


class Command(BaseCommand):
    help = 'Populate schedule with initial data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        ScheduleItem.objects.all().delete()
        
        # Create schedule items based on home page with Lucide icons
        schedules = [
            {
                'start_time': time(9, 0),
                'end_time': time(10, 0),
                'title': 'রিপোর্টিং ও সকালের নাস্তা',
                'description': 'সকলের উপস্থিতি নিবন্ধন, স্বাগত পানীয়, এবং বিশেষ স্যুভেনির টি-শার্ট ও গিফট সংগ্রহ। সবার সাথে দেখা হওয়ার প্রথম মুহূর্ত!',
                'icon_class': 'coffee',
                'color_class': 'icon-wrapper-orange',
                'order': 1,
            },
            {
                'start_time': time(10, 0),
                'end_time': time(11, 30),
                'title': 'উদ্বোধনী অনুষ্ঠান ও স্মৃতিচারণ',
                'description': 'প্রধান অতিথির ভাষণ, প্রাক্তন সদস্যদের স্মৃতিচারণ, পুরোনো ছবি ও ভিডিও প্রদর্শনী। সেই দিনগুলো ফিরে আসবে!',
                'icon_class': 'mic',
                'color_class': 'icon-wrapper-purple',
                'order': 2,
            },
            {
                'start_time': time(13, 30),
                'end_time': time(14, 30),
                'title': 'দুপুরের খাবার ও নামাজ',
                'description': 'বিশেষ বুফে লাঞ্চ - কাচ্চি বিরিয়ানি, চিকেন রোস্ট, এবং আরও অনেক কিছু! খাবারের পাশাপাশি গল্প আর হাসি।',
                'icon_class': 'utensils',
                'color_class': 'icon-wrapper-green',
                'order': 3,
            },
            {
                'start_time': time(16, 0),
                'end_time': time(17, 0),
                'title': 'সমাপনী ও র‍্যাফেল ড্র',
                'description': 'আকর্ষণীয় পুরস্কার বিতরণ, র‍্যাফেল ড্র, গ্রুপ ফটো সেশন এবং বিদায়ী সম্ভাষণ। শেষ হবে কিন্তু স্মৃতি থাকবে চিরকাল!',
                'icon_class': 'gift',
                'color_class': 'icon-wrapper-blue',
                'order': 4,
            },
        ]
        
        for schedule_data in schedules:
            ScheduleItem.objects.create(**schedule_data)
            self.stdout.write(self.style.SUCCESS(f'Created: {schedule_data["title"]}'))
        
        self.stdout.write(self.style.SUCCESS(f'Successfully populated {len(schedules)} schedule items'))
