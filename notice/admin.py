from django.contrib import admin
from .models import Notice, EmbedMessage


class NoticeAdmin(admin.ModelAdmin):
    list_display = ("title", "date_created",)
    ordering = ("-date_created",)
    fieldsets = (("お知らせ情報", {"fields": (
        "title",
        "content",
        "date_created",
    )}),)
    add_fieldsets = ((None, {"fields": (
        "title",
        "content",
    ),},),)


class EmbedMessageAdmin(admin.ModelAdmin):
    list_display = ("title","key",)
    ordering = ("key",)
    fieldsets = (("メッセージ情報", {"fields": (
        "title",
        "description",
        "key",
    )}),)
    add_fieldsets = ((None, {"fields": (
        "title",
        "description",
        "key",
    ),},),)


admin.site.register(Notice, NoticeAdmin)
admin.site.register(EmbedMessage, EmbedMessageAdmin)
