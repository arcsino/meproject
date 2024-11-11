from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, email, password, **extra_fields)


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
    email = models.EmailField(_("email address"), blank=True)
    discord_id = models.SlugField(
        _("Discord ID"),
        max_length=20,
        unique=True,
        help_text=_("DiscordのユーザーIDを本人確認メールの送信に利用します。"),
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("ユーザーが管理サイトにログイン可能かどうかを示します。"),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "ユーザーがアクティブかどうかを示します。"
            "アカウントを削除する代わりに選択を解除してください。"
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["discord_id"]
