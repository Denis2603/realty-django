# Generated by Django 4.0.4 on 2022-07-10 17:37

import app_user.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=16, verbose_name='Телефон')),
                ('contact', models.CharField(blank=True, max_length=200, verbose_name='Контактные данные')),
                ('ava', models.ImageField(blank=True, null=True, upload_to=app_user.models.path_for_avatar, verbose_name='фото')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]
