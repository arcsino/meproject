from django.contrib import admin
from .models import Notice


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


admin.site.register(Notice, NoticeAdmin)
