from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from users.models import UserProfile

admin.site.register(User, UserAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'birthdate']

