# Generated by Django 5.1.3 on 2024-11-17 17:24

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=63, unique=True, verbose_name="カテゴリー名"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=63, unique=True, verbose_name="教科名"),
                ),
                ("grade", models.IntegerField(verbose_name="学年")),
            ],
        ),
        migrations.CreateModel(
            name="Memo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "detail",
                    models.TextField(
                        blank=True,
                        help_text="詳しい説明などはこちらに。空欄でも可。",
                        max_length=255,
                        verbose_name="詳細",
                    ),
                ),
                (
                    "deadline",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="締め切り日"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="作成日時"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="変更日時"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reminder.category",
                        verbose_name="カテゴリー名",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reminder.subject",
                        verbose_name="教科名",
                    ),
                ),
            ],
        ),
    ]