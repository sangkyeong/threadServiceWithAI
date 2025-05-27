from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # 커스텀 필드가 admin에 보이도록 설정
    fieldsets = UserAdmin.fieldsets + (
        ('추가 정보', {
            'fields': (
                'gender',
                'age',
                'weekly_avg_reading_time',
                'annual_reading_amount',
                'profile_img',
                'interested_genres',
                'followings',
            ),
        }),
    )
    filter_horizontal = ('interested_genres', 'followings')
