# Generated by Django 4.0.4 on 2022-07-10 17:37

import app_realty.models
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
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='Описание')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Стоимость')),
                ('actual', models.BooleanField(default=True, verbose_name='Предложение активно')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house', to=settings.AUTH_USER_MODEL, verbose_name='Собственник')),
            ],
            options={
                'verbose_name': 'Жилье',
                'verbose_name_plural': 'Жилье',
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Количество комнат')),
                ('description', models.CharField(blank=True, max_length=150, verbose_name='Описание комнат')),
            ],
            options={
                'verbose_name': 'Комнаты',
                'verbose_name_plural': 'Комнаты',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='Тип жилья')),
                ('description', models.CharField(blank=True, max_length=150, verbose_name='Описание типа')),
            ],
            options={
                'verbose_name': 'Тип жилья',
                'verbose_name_plural': 'Типы жилья',
            },
        ),
        migrations.CreateModel(
            name='HouseFoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to=app_realty.models.path_for_foto, verbose_name='Фотография')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foto', to='app_realty.house', verbose_name='Жилье')),
            ],
            options={
                'verbose_name': 'фотография',
                'verbose_name_plural': 'фотографии',
            },
        ),
        migrations.AddField(
            model_name='house',
            name='rooms',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='house', to='app_realty.rooms', verbose_name='Комнаты'),
        ),
        migrations.AddField(
            model_name='house',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='house', to='app_realty.type', verbose_name='Тип жилья'),
        ),
    ]
