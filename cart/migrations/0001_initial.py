# Generated by Django 4.0.6 on 2022-08-16 03:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='수량')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='수정 날짜')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]
