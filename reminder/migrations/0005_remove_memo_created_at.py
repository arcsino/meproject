# Generated by Django 5.1.3 on 2024-11-17 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reminder", "0004_alter_memo_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="memo",
            name="created_at",
        ),
    ]
