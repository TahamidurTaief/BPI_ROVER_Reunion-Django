from django.core.management.base import BaseCommand
from faq.models import FAQ


class Command(BaseCommand):
    help = 'Populate FAQ with initial data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        FAQ.objects.all().delete()
        
        faqs = [
            {
                'question': 'রেজিস্ট্রেশন ফি কত?',
                'answer': '''<div class="space-y-3 sm:space-y-4 mt-2">
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 sm:gap-4">
                        <div class="flex flex-col sm:flex-row items-start sm:items-center gap-2 p-3 sm:p-4 rounded-lg sm:rounded-xl border hover:scale-105 transition-transform" style="background: rgba(139, 92, 246, 0.1); border-color: #8b5cf6;">
                            <span class="badge badge-ex-student text-xs sm:text-sm whitespace-nowrap">প্রাক্তন রোভার</span>
                            <span class="font-bold text-lg sm:text-xl" style="color: #8b5cf6;">৫০০ টাকা</span>
                        </div>
                        <div class="flex flex-col sm:flex-row items-start sm:items-center gap-2 p-3 sm:p-4 rounded-lg sm:rounded-xl border hover:scale-105 transition-transform" style="background: rgba(245, 158, 11, 0.1); border-color: #f59e0b;">
                            <span class="badge badge-teacher text-xs sm:text-sm whitespace-nowrap">স্পাউস/গেস্ট</span>
                            <span class="font-bold text-lg sm:text-xl" style="color: #f59e0b;">৪০০ টাকা</span>
                        </div>
                        <div class="flex flex-col sm:flex-row items-start sm:items-center gap-2 p-3 sm:p-4 rounded-lg sm:rounded-xl border hover:scale-105 transition-transform" style="background: rgba(16, 185, 129, 0.1); border-color: #10b981;">
                            <span class="badge badge-student text-xs sm:text-sm whitespace-nowrap">শিশু (৫ বছর+)</span>
                            <span class="font-bold text-lg sm:text-xl" style="color: #10b981;">৩০০ টাকা</span>
                        </div>
                    </div>
                </div>''',
                'icon_class': 'dollar-sign',
                'style_class': 'faq-item-purple',
                'is_important': True,
                'is_expanded_by_default': True,
                'order': 1,
            },
            {
                'question': 'আমি কি স্পট রেজিস্ট্রেশন করতে পারব?',
                'answer': '''<div class="space-y-3 sm:space-y-4 mt-2">
                    <div class="p-3 sm:p-4 rounded-lg sm:rounded-xl border-l-4" style="background: rgba(239, 68, 68, 0.1); border-color: #ef4444;">
                        <p class="flex items-start gap-2">
                            <strong>না, দুঃখিত।</strong> খাবারের আয়োজন এবং উপহার নিশ্চিত করার জন্য আমাদের আগে থেকেই রেজিস্ট্রেশন বন্ধ করতে হবে।
                        </p>
                    </div>
                </div>''',
                'icon_class': 'file-text',
                'style_class': 'faq-item-blue',
                'order': 2,
            },
            {
                'question': 'আমি কি আমার পরিবারকে সাথে আনতে পারব?',
                'answer': '''<div class="space-y-3 sm:space-y-4 mt-2">
                    <div class="p-3 sm:p-4 rounded-lg sm:rounded-xl border-l-4" style="background: rgba(16, 185, 129, 0.1); border-color: #10b981;">
                        <p class="flex items-start gap-2">
                            <strong>হ্যাঁ, অবশ্যই!</strong> পরিবারের সবাইকে নিয়ে আসুন। আপনার প্রিয়জনদের সাথে এই বিশেষ মুহূর্তগুলো শেয়ার করুন।
                        </p>
                    </div>
                </div>''',
                'icon_class': 'users',
                'style_class': 'faq-item-green',
                'order': 3,
            },
            {
                'question': 'পেমেন্ট কিভাবে করব?',
                'answer': '''<div class="space-y-3 sm:space-y-4 mt-2">
                    <p class="font-medium">রেজিস্ট্রেশন সম্পন্ন করার পর আপনাকে পেমেন্ট অপশন দেখানো হবে। পেমেন্ট পদ্ধতি:</p>
                    <ul class="list-disc list-inside space-y-2">
                        <li>মোবাইল ব্যাংকিং (বিকাশ / নগদ / রকেট)</li>
                        <li>ব্যাংক ট্রান্সফার</li>
                        <li>ক্যাশ পেমেন্ট (নির্দিষ্ট সংগ্রাহকের কাছে)</li>
                    </ul>
                </div>''',
                'icon_class': 'credit-card',
                'style_class': 'faq-item-orange',
                'order': 4,
            },
        ]
        
        for faq_data in faqs:
            FAQ.objects.create(**faq_data)
            self.stdout.write(self.style.SUCCESS(f'Created FAQ: {faq_data["question"]}'))
        
        self.stdout.write(self.style.SUCCESS(f'Successfully populated {len(faqs)} FAQ items'))
