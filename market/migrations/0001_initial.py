# Generated by Django 4.0.6 on 2022-08-10 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

from market.gen_master_data import gen_master


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='마켓 이름')),
                ('site_url', models.URLField(max_length=100, verbose_name='마켓 사이트')),
                ('email', models.EmailField(max_length=100, verbose_name='마켓 이메일')),
                ('description', models.TextField(verbose_name='마켓 설명')),
                ('review_point', models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='리뷰 포인트')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='수정 날짜')),
                ('master', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(blank=True, to='tag.tag')),
            ],
            options={
                'db_table': 'market',
            },
        ),
        migrations.RunPython(gen_master),
    ]
