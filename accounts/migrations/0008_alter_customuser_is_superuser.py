# Generated by Django 5.1.3 on 2024-11-12 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customuser_discord_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='ユーザーがスーパーユーザーかどうかを示します。', verbose_name='superuer'),
        ),
    ]
