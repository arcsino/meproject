# Generated by Django 5.1.3 on 2024-11-22 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0017_customuser_schedule_id_alter_customuser_subject"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="subject",
        ),
        migrations.DeleteModel(
            name="TakingSubject",
        ),
    ]