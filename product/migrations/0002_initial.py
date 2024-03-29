# Generated by Django 4.0.6 on 2022-08-16 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions

from product.gen_product_data import gen_product_data


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('market', '0001_initial'),
        ('product', '0001_initial'),
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='productlikeuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='market',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='market.market'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_like_user',
            field=models.ManyToManyField(related_name='product_like_user', through='product.ProductLikeUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='productreal',
            constraint=models.UniqueConstraint(django.db.models.expressions.F('product'), django.db.models.expressions.F('option_1_name'), django.db.models.expressions.F('option_2_name'), django.db.models.expressions.F('option_3_name'), name='option_name_unique'),
        ),
        migrations.RunPython(gen_product_data),
    ]
