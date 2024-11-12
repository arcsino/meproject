from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def _create_user(self, username, discord_id, password, **extra_fields):
        if not username:
            raise ValueError("この項目は必須です。")
        user = self.model(username=username, discord_id=discord_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, discord_id=None, password=None, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, discord_id, password, **extra_fields)

    def create_superuser(self, username, discord_id=None, password=None, **extra_fields):
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True

        if extra_fields.get("is_staff") is not True:
            raise ValueError("スーパーユーザーには is_staff=True が必要です。")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("スーパーユーザーには is_superuser=True が必要です。")

        return self._create_user(username, discord_id, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "この項目は必須です。半角アルファベット、半角数字、@/./+/-/_ で150文字以下にしてください。"
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("同じユーザー名が既に登録済みです。"),
        },
    )
    discord_username = models.CharField(
        _("Discordのユーザー名"),
        max_length=20,
        unique=True,
        help_text=_("Discordのユーザー名を本人確認に利用します。"),
    )
    is_superuser = models.BooleanField(
        _("superuer"),
        default=False,
        help_text=_("ユーザーがスーパーユーザーかどうかを示します。"),
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("ユーザーが管理サイトにログイン可能かどうかを示します。"),
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "ユーザーがアクティブかどうかを示します。"
            "アカウントを削除する代わりに選択を解除してください。"
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["discord_id"]
