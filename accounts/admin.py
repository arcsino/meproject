from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import TakingSubject, DiscordUser


User = get_user_model()
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "discord_id",
        "is_staff",
        "is_active",
    )
    search_fields = ("username", "discord_id")
    ordering = ("id",)
    fieldsets = (("ユーザー情報", {"fields": (
        "username",
        "discord_id",
        "password",
        "is_staff",
        "is_active",
        "date_joined",
        "subject",
    )}),)
    add_fieldsets = ((None, {"fields": (
        "username",
        "discord_id",
        "password1", 
        "password2",
    ),},),)


class DiscordUserAdmin(admin.ModelAdmin):
    list_display = ("username", "discord_id",)
    ordering = ("id",)
    fieldsets = (("ユーザー情報", {"fields": (
        "username",
        "discord_id",
    )}),)
    add_fieldsets = ((None, {"fields": (
        "username",
        "discord_id",
    ),},),)


class TakingSubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "grade", "_num_of_taken_by")
    ordering = ("id",)
    fieldsets = (("履修中教科の情報", {"fields": (
        "name",
        "grade",
    )}),)
    add_fieldsets = ((None, {"fields": (
        "name",
        "grade",
    ),},),)
    # _num_of_taken_by: 履修中者の数
    def _num_of_taken_by(self, obj):
        return User.objects.filter(subject=obj).count()


admin.site.register(User, CustomUserAdmin)
admin.site.register(DiscordUser, DiscordUserAdmin)
admin.site.register(TakingSubject, TakingSubjectAdmin)
