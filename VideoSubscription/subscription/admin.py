from django.contrib import admin
from .models import User, Video, Subscription
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'phone_number','subscribe']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'discription', 'subscription_type', 'image', 'video']

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'membership_type', 'expiry_date']