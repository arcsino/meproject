# Generated by Django 5.1.3 on 2024-11-18 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reminder", "0005_remove_memo_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="memo",
            name="detail",
            field=models.TextField(
                blank=True,
                help_text="詳しい説明などはこちらに。空欄でも可。",
                null=True,
                verbose_name="詳細",
            ),
        ),
    ]