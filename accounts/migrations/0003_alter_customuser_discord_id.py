# Generated by Django 5.1.3 on 2024-11-09 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_discord_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='discord_id',
            field=models.SlugField(max_length=20, unique=True, verbose_name='discord id'),
        ),
    ]
