from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'mobile']
    search_fields = ['user']

admin.site.register(UserProfile,UserProfileAdmin)