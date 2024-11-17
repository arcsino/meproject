from django.contrib import admin
from .models import Category, Subject, Memo


class CategoryAdmin(admin.ModelAdmin):

    list_display = ("title", "_num_of_category_memo")
    ordering = ("id",)

    # _num_of_category_memo: 特定のカテゴリー名で設定されたリマインダーの数
    def _num_of_category_memo(self, obj):
        return Memo.objects.filter(category=obj).count()


class SubjectAdmin(admin.ModelAdmin):

    list_display = ("title", "_num_of_subject_memo")
    ordering = ("id",)

    # _num_of_subject_memo: 特定の教科名名で設定されたリマインダーの数
    def _num_of_subject_memo(self, obj):
        return Memo.objects.filter(subject=obj).count()


class MemoAdmin(admin.ModelAdmin):
    
    list_display = ("title", "subject", "category", "deadline", "updated_at")
    ordering = ("deadline",)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Memo, MemoAdmin)
