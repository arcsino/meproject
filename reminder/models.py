from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        _("カテゴリー名"),
        max_length=64,
        unique=True,
    )
    bs_color = models.CharField(_("Boostrap Color"), max_length=32)
    bs_icon = models.CharField(_("Bootstrap Icon"), max_length=32)
    channel_id = models.SlugField(_("チャンネルID"), max_length=20)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(
        _("教科名"),
        max_length=64,
        unique=True,
    )
    grade = models.IntegerField(
        _("学年"),
    )

    def __str__(self):
        return self.name


class Schedule(models.Model):
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
        max_length=64,
        help_text=_(
            "課題プリント、中間テスト、証明写真など"
        ),
    )
    detail = models.TextField(
        _("詳細"),
        blank=True,
        null=True,
        help_text=_(
            "詳しい説明などはこちらに。空欄でも可。"
        ),
    )
    deadline = models.DateField(
        _("締め切り日"),
        help_text=_(
            "20XX-XX-XX"
        ),
    )
    created_by = models.CharField(
        _("作成者"),
        max_length=64,
        default=_("unknown")
    )
    created_at = models.DateTimeField(
        _("作成日時"),
        default=timezone.now,
    )
    updated_by = models.CharField(
        _("編集者"),
        max_length=64,
        default=_("unknown"),
    )
    updated_at = models.DateTimeField(
        _("変更日時"),
        default=timezone.now,
    )

    def __str__(self):
        return self.title
