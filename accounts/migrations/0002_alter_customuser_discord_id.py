# Generated by Django 5.1.3 on 2024-11-09 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='discord_id',
            field=models.IntegerField(unique=True, verbose_name='discord id'),
        ),
    ]
