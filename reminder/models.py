from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from accounts.models import CustomUser


class Category(models.Model):
    name = models.CharField(
        _("カテゴリー名"),
        max_length=64,
        unique=True,
    )
    bs_color = models.CharField(_("Boostrap Color"), max_length=32)
    bs_icon = models.CharField(_("Bootstrap Icon"), max_length=32)
    webhook_url = models.CharField(_("Webhook Url"), max_length=128)
    embed_color = models.CharField(_("embed_color"), max_length=16, default="green")

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


class Deadline(models.Model):
    date = models.DateField(
        _("締め切り日"),
        unique=True,
    )
    MON = "月曜日"
    TUE = "火曜日"
    WED = "水曜日"
    THU = "木曜日"
    FRI = "金曜日"
    SAT = "土曜日"
    SUN = "日曜日"
    WEEK_CHOICES = {
        MON: "月曜日",
        TUE: "火曜日",
        WED: "水曜日",
        THU: "木曜日",
        FRI: "金曜日",
        SAT: "土曜日",
        SUN: "日曜日",
    }
    week = models.CharField(
        _("曜日"),
        max_length=3,
        choices=WEEK_CHOICES,
        default=MON
    )

    def __str__(self):
        return self.date.strftime("%Y年%m月%d日") + f"（{self.week}）"


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
    deadline = models.ForeignKey(
        Deadline,
        verbose_name="締め切り日",
        on_delete=models.CASCADE,
    )
    created_by = models.CharField(
        _("作成者"),
        max_length=64,
        default=_("unknown")
    )
    created_at = models.DateTimeField(
        _("作成日時"),
        auto_now_add=True,
    )
    updated_by = models.CharField(
        _("編集者"),
        max_length=64,
        default=_("unknown"),
    )
    updated_at = models.DateTimeField(
        _("変更日時"),
        auto_now=True,
    )
    finished_user = models.ManyToManyField(
        CustomUser,
        verbose_name="完遂ユーザー",
        blank=True,
    )

    def __str__(self):
        return self.title
