from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Notice(models.Model):
    title = models.CharField(
        _("Notice title"),
        max_length=127,
        help_text=_(
            "お知らせのタイトル"
        ),
    )
    content = models.TextField(
        _("Notice content"),
        blank=True,
        help_text=_(
            "お知らせの内容"
        ),
    )
    date_created = models.DateTimeField(_("date created"), default=timezone.now)


class EmbedMessage(models.Model):
    title = models.CharField(
        _("Title"),
        max_length=64,
        blank=True,
        null=True,
    )
    description = models.TextField(
        _("description"),
        max_length=512,
        blank=True,
        null=True,
    )
    key = models.IntegerField(
        _("key"),
        unique=True,
    )
