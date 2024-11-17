from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(
        _("カテゴリー名"),
        max_length=63,
        unique=True,
    )

    def __str__(self):
        return self.title


class Subject(models.Model):
    title = models.CharField(
        _("教科名"),
        max_length=63,
        unique=True,
    )
    grade = models.IntegerField(
        _("学年"),
    )

    def __str__(self):
        return self.title


class Memo(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name="カテゴリー名",
        on_delete=models.CASCADE,
    )
    subject = models.ForeignKey(
        Subject,
        verbose_name="教科名",
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        _("タイトル名"),
        max_length=63,
        help_text=_(
            "課題プリント、中間テスト、証明写真など"
        ),
    )
    detail = models.TextField(
        _("詳細"),
        blank=True,
        help_text=_(
            "詳しい説明などはこちらに。空欄でも可。"
        ),
    )
    deadline = models.DateField(
        _("締め切り日"),
        default=timezone.now,
    )
    updated_at = models.DateTimeField(
        _("変更日時"),
        auto_now=True,
    )

    def __str__(self):
        return self.title
