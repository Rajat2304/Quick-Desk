from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Add the 'role' field to the user list display
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')
    # Add the 'role' field to the editing form for a user
    fieldsets = UserAdmin.fieldsets + (
        ('Role', {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role', {'fields': ('role',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
