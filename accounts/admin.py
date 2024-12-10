from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


User = get_user_model()

class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "nickname",
        "is_staff",
        "is_active",
        "id"
    )
    search_fields = ("username",)
    fieldsets = (("ユーザー情報", {"fields": (
        "username",
        "nickname",
        "password",
        "is_staff",
        "is_active",
        "date_joined",
    )}),)
    add_fieldsets = ((None, {"fields": (
        "username",
        "nickname",
        "password1", 
        "password2",
    ),},),)


admin.site.register(User, CustomUserAdmin)
