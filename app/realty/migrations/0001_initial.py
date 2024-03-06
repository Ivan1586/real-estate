# Generated by Django 5.0.2 on 2024-03-06 09:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('square', models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Общая площадь')),
                ('living_space', models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Жилая площадь')),
                ('kitchen_area', models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Площадь кухни')),
                ('rooms', models.PositiveSmallIntegerField(verbose_name='Количество комнат')),
                ('floor', models.PositiveSmallIntegerField(verbose_name='Этаж')),
                ('status', models.CharField(choices=[('On sale', 'В продаже'), ('Sold', 'Продана')], default='On sale', max_length=7, verbose_name='Статус')),
                ('price', models.PositiveBigIntegerField(verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
