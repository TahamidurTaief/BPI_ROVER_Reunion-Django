from django.core.management.base import BaseCommand
from terms.models import TermsAndConditions


class Command(BaseCommand):
    help = 'Populate Terms and Conditions with initial data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        TermsAndConditions.objects.all().delete()
        
        terms = [
            {
                'title': 'অফেরতযোগ্য রেজিস্ট্রেশন',
                'description': 'সকল রেজিস্ট্রেশন সম্পূর্ণ অফেরতযোগ্য। একবার নিবন্ধন সম্পন্ন হলে কোনো অবস্থাতেই টাকা ফেরত দেওয়া হবে না।',
                'icon_class': 'alert-triangle',
                'icon_color_class': 'text-error',
                'is_critical': True,
                'order': 1,
            },
            {
                'title': 'সময়মত পেমেন্ট',
                'description': 'নির্ধারিত সময়ের মধ্যে পেমেন্ট সম্পন্ন করতে হবে, অন্যথায় রেজিস্ট্রেশন স্বয়ংক্রিয়ভাবে বাতিল বলে গণ্য হবে এবং আপনার স্লট অন্যকে দেওয়া হবে।',
                'icon_class': 'clock-alert',
                'icon_color_class': 'text-warning',
                'is_critical': True,
                'order': 2,
            },
            {
                'title': 'নিষিদ্ধ কার্যকলাপ',
                'description': 'অনুষ্ঠানস্থলে যেকোনো ধরনের রাজনৈতিক, ধর্মীয় বিতর্ক বা অসামাজিক কার্যকলাপ সম্পূর্ণ নিষিদ্ধ। এটি একটি পারিবারিক অনুষ্ঠান।',
                'icon_class': 'ban',
                'icon_color_class': 'text-error',
                'order': 3,
            },
            {
                'title': 'কর্তৃপক্ষের অধিকার',
                'description': 'কর্তৃপক্ষ যেকোনো সময়, যেকোনো সিদ্ধান্ত পরিবর্তন, পরিমার্জন বা সংশোধন করার সম্পূর্ণ অধিকার সংরক্ষণ করে।',
                'icon_class': 'file-check',
                'icon_color_class': 'text-info',
                'order': 4,
            },
            {
                'title': 'ব্যক্তিগত দায়িত্ব',
                'description': 'অনুষ্ঠানস্থলে আপনার শিশু এবং ব্যক্তিগত সামগ্রীর সম্পূর্ণ দায়িত্ব আপনার। কোনো কিছু হারিয়ে গেলে বা ক্ষতিগ্রস্ত হলে কর্তৃপক্ষ কোনোভাবেই দায়ী থাকবে না।',
                'icon_class': 'backpack',
                'icon_color_class': 'text-accent',
                'order': 5,
            },
            {
                'title': 'ফটোগ্রাফি ও ভিডিও',
                'description': 'অনুষ্ঠানের ছবি ও ভিডিও প্রচারণামূলক উদ্দেশ্যে ব্যবহার করা হতে পারে। রেজিস্ট্রেশন করার মাধ্যমে আপনি এতে সম্মতি প্রদান করছেন।',
                'icon_class': 'camera',
                'icon_color_class': 'text-primary',
                'order': 6,
            },
        ]
        
        for term_data in terms:
            TermsAndConditions.objects.create(**term_data)
            self.stdout.write(self.style.SUCCESS(f'Created term: {term_data["title"]}'))
        
        self.stdout.write(self.style.SUCCESS(f'Successfully populated {len(terms)} terms'))
