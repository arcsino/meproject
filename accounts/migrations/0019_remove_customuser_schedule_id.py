# Generated by Django 5.1.3 on 2024-11-22 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0018_remove_customuser_subject_delete_takingsubject"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="schedule_id",
        ),
    ]