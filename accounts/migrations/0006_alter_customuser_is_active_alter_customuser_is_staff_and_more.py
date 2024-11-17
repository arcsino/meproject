# Generated by Django 5.1.3 on 2024-11-11 16:02

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customuser_discord_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='ユーザーがアクティブかどうかを示します。アカウントを削除する代わりに選択を解除してください。', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='ユーザーが管理サイトにログイン可能かどうかを示します。', verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': '同じユーザー名が既に登録済みです。'}, help_text='この項目は必須です。半角アルファベット、半角数字、@/./+/-/_ で150文字以下にしてください。', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
