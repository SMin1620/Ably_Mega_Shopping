# Generated by Django 4.0.6 on 2022-08-16 03:45

from django.db import migrations, models
import django.db.models.deletion

from product.gen_product_data import gen_product_data


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='카테고리명')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='상품명(내부용)')),
                ('display_name', models.CharField(max_length=100, verbose_name='상품명(노출용)')),
                ('description', models.TextField(verbose_name='상품 설명')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='권장 판매가')),
                ('sale_price', models.PositiveIntegerField(default=0, verbose_name='실제 판매가')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='숨김 여부')),
                ('is_sold_out', models.BooleanField(default=False, verbose_name='품절 여부')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='삭제 여부')),
                ('delete_date', models.DateTimeField(blank=True, null=True, verbose_name='삭제 날짜')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='수정 날짜')),
                ('hit_count', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('review_count', models.PositiveIntegerField(default=0, verbose_name='리뷰수')),
                ('review_point', models.PositiveIntegerField(default=0, verbose_name='리뷰 평점')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductReal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_1_type', models.CharField(default='SIZE', max_length=10, verbose_name='옵션1 타입')),
                ('option_1_name', models.CharField(max_length=30, verbose_name='옵션1 이름 (내부용)')),
                ('option_1_display_name', models.CharField(max_length=30, verbose_name='옵션1 이름 (노출용)')),
                ('option_2_type', models.CharField(default='COLOR', max_length=10, verbose_name='옵션2 타입')),
                ('option_2_name', models.CharField(max_length=30, verbose_name='옵션2 이름 (내부용)')),
                ('option_2_display_name', models.CharField(max_length=30, verbose_name='옵션2 이름 (노출용)')),
                ('option_3_type', models.CharField(blank=True, default='', max_length=10, verbose_name='옵션3 타입')),
                ('option_3_name', models.CharField(blank=True, max_length=30, verbose_name='옵션3 이름 (내부용)')),
                ('option_3_display_name', models.CharField(blank=True, max_length=30, verbose_name='옵션3 이름 (노출용)')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='수정 날짜')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='숨김 여부')),
                ('is_sold_out', models.BooleanField(default=False, verbose_name='품절 여부')),
                ('add_price', models.PositiveIntegerField(default=0, verbose_name='추가 가격')),
                ('stock_quantity', models.PositiveIntegerField(default=0, verbose_name='재고량')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_real', to='product.product')),
            ],
            options={
                'db_table': 'product_real',
            },
        ),
        migrations.CreateModel(
            name='ProductLikeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='수정 날짜')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'product_like_user',
            },
        ),
    ]
