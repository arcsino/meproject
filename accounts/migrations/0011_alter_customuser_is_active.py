# Generated by Django 5.1.3 on 2024-11-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_rename_discord_id_customuser_discord_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False, help_text='ユーザーがアクティブかどうかを示します。アカウントを削除する代わりに選択を解除してください。', verbose_name='active'),
        ),
    ]