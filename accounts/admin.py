from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


User = get_user_model()

class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "is_staff",
        "is_active",
    )
    search_fields = ("username",)
    ordering = ("id",)
    fieldsets = (("ユーザー情報", {"fields": (
        "username",
        "password",
        "is_staff",
        "is_active",
        "date_joined",
    )}),)
    add_fieldsets = ((None, {"fields": (
        "username",
        "password1", 
        "password2",
    ),},),)


admin.site.register(User, CustomUserAdmin)
