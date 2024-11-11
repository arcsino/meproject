from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


User = get_user_model()
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "discord_id",
        "is_staff",
        "is_active",
    )

    search_fields = ("username", "discord_id")

    ordering = ("username",)

    fieldsets = (("ユーザー情報", {"fields": ("username", "discord_id", "password", "is_staff", "is_active", "date_joined")}),)

    add_fieldsets = (
        (
            None,
            {
                "fields": ("username", "discord_id", "password1", "password2"),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
