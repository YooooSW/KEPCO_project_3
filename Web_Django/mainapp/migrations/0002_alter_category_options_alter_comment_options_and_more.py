# Generated by Django 4.0.1 on 2023-06-12 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='community',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='google_account',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='kakao_account',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='naver_account',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='provision',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='provision_history',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='user_img',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='user_service',
            options={'managed': True},
        ),
    ]