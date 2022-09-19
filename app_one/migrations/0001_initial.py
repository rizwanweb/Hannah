# Generated by Django 4.0 on 2022-09-17 20:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Cosmetics_brand_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cosmetics_brand_image_get', models.ImageField(blank=True, null=True, upload_to='')),
                ('Cosmetics_brand_image_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 18, 2, 48, 56, 73028))),
            ],
            options={
                'verbose_name_plural': 'Cosmetics brand image',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Newsletter_name', models.CharField(blank=True, max_length=256, null=True)),
                ('Newsletter_mobile_number', models.TextField(blank=True, null=True)),
                ('Newsletter_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 18, 2, 48, 56, 72030))),
            ],
            options={
                'verbose_name_plural': 'Newsletter',
            },
        ),
        migrations.CreateModel(
            name='Picture_slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Picture_Title', models.CharField(blank=True, max_length=256, null=True)),
                ('Picture_upload', models.ImageField(blank=True, null=True, upload_to='')),
                ('Picture_content', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Banner Picture slide',
            },
        ),
        migrations.CreateModel(
            name='Product_Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Brand_name', models.CharField(blank=True, max_length=256, null=True)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='banner_image/')),
            ],
            options={
                'verbose_name_plural': 'Product Brand',
            },
        ),
        migrations.CreateModel(
            name='Product_Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Color_name', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'verbose_name_plural': 'Product Color',
            },
        ),
        migrations.CreateModel(
            name='Product_Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Size_name', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'verbose_name_plural': 'Product Size',
            },
        ),
        migrations.CreateModel(
            name='Stay_Updated_subscribtion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stay_Updated_mobile_number', models.TextField(blank=True, null=True)),
                ('Stay_Updated_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 18, 2, 48, 56, 72030))),
            ],
            options={
                'verbose_name_plural': 'Stay Updated subscribtion',
            },
        ),
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(blank=True, max_length=256, null=True)),
                ('User_mobile', models.CharField(blank=True, max_length=256, null=True)),
                ('User_pass', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'verbose_name_plural': 'User info',
            },
        ),
        migrations.CreateModel(
            name='Video_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video_Title', models.CharField(blank=True, max_length=256, null=True)),
                ('Video_Link', models.TextField(blank=True, null=True)),
                ('Video_content', models.TextField(blank=True, null=True)),
                ('Blog_podt_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 18, 2, 48, 56, 72030))),
            ],
            options={
                'verbose_name_plural': 'Video Post',
            },
        ),
        migrations.CreateModel(
            name='Product_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Title', models.CharField(blank=True, max_length=256, null=True)),
                ('Product_Picture_upload_1', models.ImageField(blank=True, help_text='Insert 500X500 pixel image', null=True, upload_to='')),
                ('Product_Picture_upload_2', models.ImageField(blank=True, help_text='Insert 500X500 pixel image', null=True, upload_to='')),
                ('Product_Picture_upload_3', models.ImageField(blank=True, help_text='Insert 500X500 pixel image', null=True, upload_to='')),
                ('Product_Picture_upload_4', models.ImageField(blank=True, help_text='Insert 500X500 pixel image', null=True, upload_to='')),
                ('Product_Picture_upload_5', models.ImageField(blank=True, help_text='Insert 500X500 pixel image', null=True, upload_to='')),
                ('Product_short_details', models.CharField(blank=True, max_length=256, null=True)),
                ('Product_long_details', models.TextField(blank=True, null=True)),
                ('Product_Additional_Information', models.TextField(blank=True, null=True)),
                ('Product_Size_Get', models.CharField(blank=True, max_length=256, null=True)),
                ('Product_Country', models.CharField(blank=True, max_length=256, null=True)),
                ('Product_Sell_Prize', models.IntegerField(blank=True, null=True)),
                ('Product_Discount_Prize', models.IntegerField(default=0)),
                ('Product_show_type', models.CharField(blank=True, choices=[('', ''), ('You May Also Like', 'You May Also Like'), ('Trandy Products', 'Trandy Products')], max_length=256, null=True)),
                ('Product_Category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_one.category')),
                ('Product_brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_one.product_brand')),
                ('Product_color_Get', models.ManyToManyField(blank=True, null=True, to='app_one.Product_Color')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Order_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_No', models.IntegerField(blank=True, null=True)),
                ('perchase_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 18, 2, 48, 56, 76020))),
                ('order_User_Name', models.CharField(blank=True, max_length=256, null=True)),
                ('order_User_Mobile', models.CharField(blank=True, max_length=256, null=True)),
                ('order_User_Address', models.CharField(blank=True, max_length=256, null=True)),
                ('order_User_City', models.CharField(blank=True, max_length=256, null=True)),
                ('order_User_ZIP', models.CharField(blank=True, max_length=256, null=True)),
                ('order_User_shipping_charge', models.CharField(blank=True, max_length=256, null=True)),
                ('order_User_Sub_total', models.CharField(blank=True, max_length=256, null=True)),
                ('order_User_total', models.CharField(blank=True, max_length=256, null=True)),
                ('Name_of_product_1', models.CharField(blank=True, max_length=256, null=True)),
                ('product_1_quantity', models.CharField(blank=True, max_length=256, null=True)),
                ('product_1_Price', models.CharField(blank=True, max_length=256, null=True)),
                ('product_1_image_link', models.CharField(blank=True, max_length=256, null=True)),
                ('product_1_brand', models.CharField(blank=True, max_length=256, null=True)),
                ('product_1_size', models.CharField(blank=True, max_length=256, null=True)),
                ('product_1_color', models.CharField(blank=True, max_length=256, null=True)),
                ('Name_of_product_2', models.CharField(blank=True, max_length=256, null=True)),
                ('product_2_quantity', models.CharField(blank=True, max_length=256, null=True)),
                ('product_2_Price', models.CharField(blank=True, max_length=256, null=True)),
                ('product_2_image_link', models.CharField(blank=True, max_length=256, null=True)),
                ('product_2_brand', models.CharField(blank=True, max_length=256, null=True)),
                ('product_2_size', models.CharField(blank=True, max_length=256, null=True)),
                ('product_2_color', models.CharField(blank=True, max_length=256, null=True)),
                ('Name_of_product_3', models.CharField(blank=True, max_length=356, null=True)),
                ('product_3_quantity', models.CharField(blank=True, max_length=356, null=True)),
                ('product_3_Price', models.CharField(blank=True, max_length=356, null=True)),
                ('product_3_image_link', models.CharField(blank=True, max_length=356, null=True)),
                ('product_3_brand', models.CharField(blank=True, max_length=356, null=True)),
                ('product_3_size', models.CharField(blank=True, max_length=356, null=True)),
                ('product_3_color', models.CharField(blank=True, max_length=356, null=True)),
                ('Name_of_product_4', models.CharField(blank=True, max_length=456, null=True)),
                ('product_4_quantity', models.CharField(blank=True, max_length=456, null=True)),
                ('product_4_Price', models.CharField(blank=True, max_length=456, null=True)),
                ('product_4_image_link', models.CharField(blank=True, max_length=456, null=True)),
                ('product_4_brand', models.CharField(blank=True, max_length=456, null=True)),
                ('product_4_size', models.CharField(blank=True, max_length=456, null=True)),
                ('product_4_color', models.CharField(blank=True, max_length=456, null=True)),
                ('Name_of_product_5', models.CharField(blank=True, max_length=556, null=True)),
                ('product_5_quantity', models.CharField(blank=True, max_length=556, null=True)),
                ('product_5_Price', models.CharField(blank=True, max_length=556, null=True)),
                ('product_5_image_link', models.CharField(blank=True, max_length=556, null=True)),
                ('product_5_brand', models.CharField(blank=True, max_length=556, null=True)),
                ('product_5_size', models.CharField(blank=True, max_length=556, null=True)),
                ('product_5_color', models.CharField(blank=True, max_length=556, null=True)),
                ('Name_of_product_6', models.CharField(blank=True, max_length=66, null=True)),
                ('product_6_quantity', models.CharField(blank=True, max_length=66, null=True)),
                ('product_6_Price', models.CharField(blank=True, max_length=66, null=True)),
                ('product_6_image_link', models.CharField(blank=True, max_length=66, null=True)),
                ('product_6_brand', models.CharField(blank=True, max_length=66, null=True)),
                ('product_6_size', models.CharField(blank=True, max_length=66, null=True)),
                ('product_6_color', models.CharField(blank=True, max_length=66, null=True)),
                ('Name_of_product_7', models.CharField(blank=True, max_length=7, null=True)),
                ('product_7_quantity', models.CharField(blank=True, max_length=7, null=True)),
                ('product_7_Price', models.CharField(blank=True, max_length=7, null=True)),
                ('product_7_image_link', models.CharField(blank=True, max_length=7, null=True)),
                ('product_7_brand', models.CharField(blank=True, max_length=7, null=True)),
                ('product_7_size', models.CharField(blank=True, max_length=7, null=True)),
                ('product_7_color', models.CharField(blank=True, max_length=7, null=True)),
                ('Name_of_product_8', models.CharField(blank=True, max_length=8, null=True)),
                ('product_8_quantity', models.CharField(blank=True, max_length=8, null=True)),
                ('product_8_Price', models.CharField(blank=True, max_length=8, null=True)),
                ('product_8_image_link', models.CharField(blank=True, max_length=8, null=True)),
                ('product_8_brand', models.CharField(blank=True, max_length=8, null=True)),
                ('product_8_size', models.CharField(blank=True, max_length=8, null=True)),
                ('product_8_color', models.CharField(blank=True, max_length=8, null=True)),
                ('Name_of_product_9', models.CharField(blank=True, max_length=9, null=True)),
                ('product_9_quantity', models.CharField(blank=True, max_length=9, null=True)),
                ('product_9_Price', models.CharField(blank=True, max_length=9, null=True)),
                ('product_9_image_link', models.CharField(blank=True, max_length=9, null=True)),
                ('product_9_brand', models.CharField(blank=True, max_length=9, null=True)),
                ('product_9_size', models.CharField(blank=True, max_length=9, null=True)),
                ('product_9_color', models.CharField(blank=True, max_length=9, null=True)),
                ('Name_of_product_10', models.CharField(blank=True, max_length=10, null=True)),
                ('product_10_quantity', models.CharField(blank=True, max_length=10, null=True)),
                ('product_10_Price', models.CharField(blank=True, max_length=10, null=True)),
                ('product_10_image_link', models.CharField(blank=True, max_length=10, null=True)),
                ('product_10_brand', models.CharField(blank=True, max_length=10, null=True)),
                ('product_10_size', models.CharField(blank=True, max_length=10, null=True)),
                ('product_10_color', models.CharField(blank=True, max_length=10, null=True)),
                ('Name_of_product_11', models.CharField(blank=True, max_length=11, null=True)),
                ('product_11_quantity', models.CharField(blank=True, max_length=11, null=True)),
                ('product_11_Price', models.CharField(blank=True, max_length=11, null=True)),
                ('product_11_image_link', models.CharField(blank=True, max_length=11, null=True)),
                ('product_11_brand', models.CharField(blank=True, max_length=11, null=True)),
                ('product_11_size', models.CharField(blank=True, max_length=11, null=True)),
                ('product_11_color', models.CharField(blank=True, max_length=11, null=True)),
                ('Name_of_product_12', models.CharField(blank=True, max_length=12, null=True)),
                ('product_12_quantity', models.CharField(blank=True, max_length=12, null=True)),
                ('product_12_Price', models.CharField(blank=True, max_length=12, null=True)),
                ('product_12_image_link', models.CharField(blank=True, max_length=12, null=True)),
                ('product_12_brand', models.CharField(blank=True, max_length=12, null=True)),
                ('product_12_size', models.CharField(blank=True, max_length=12, null=True)),
                ('product_12_color', models.CharField(blank=True, max_length=12, null=True)),
                ('Name_of_product_13', models.CharField(blank=True, max_length=13, null=True)),
                ('product_13_quantity', models.CharField(blank=True, max_length=13, null=True)),
                ('product_13_Price', models.CharField(blank=True, max_length=13, null=True)),
                ('product_13_image_link', models.CharField(blank=True, max_length=13, null=True)),
                ('product_13_brand', models.CharField(blank=True, max_length=13, null=True)),
                ('product_13_size', models.CharField(blank=True, max_length=13, null=True)),
                ('product_13_color', models.CharField(blank=True, max_length=13, null=True)),
                ('Name_of_product_14', models.CharField(blank=True, max_length=14, null=True)),
                ('product_14_quantity', models.CharField(blank=True, max_length=14, null=True)),
                ('product_14_Price', models.CharField(blank=True, max_length=14, null=True)),
                ('product_14_image_link', models.CharField(blank=True, max_length=14, null=True)),
                ('product_14_brand', models.CharField(blank=True, max_length=14, null=True)),
                ('product_14_size', models.CharField(blank=True, max_length=14, null=True)),
                ('product_14_color', models.CharField(blank=True, max_length=14, null=True)),
                ('Name_of_product_15', models.CharField(blank=True, max_length=15, null=True)),
                ('product_15_quantity', models.CharField(blank=True, max_length=15, null=True)),
                ('product_15_Price', models.CharField(blank=True, max_length=15, null=True)),
                ('product_15_image_link', models.CharField(blank=True, max_length=15, null=True)),
                ('product_15_brand', models.CharField(blank=True, max_length=15, null=True)),
                ('product_15_size', models.CharField(blank=True, max_length=15, null=True)),
                ('product_15_color', models.CharField(blank=True, max_length=15, null=True)),
                ('Name_of_product_16', models.CharField(blank=True, max_length=16, null=True)),
                ('product_16_quantity', models.CharField(blank=True, max_length=16, null=True)),
                ('product_16_Price', models.CharField(blank=True, max_length=16, null=True)),
                ('product_16_image_link', models.CharField(blank=True, max_length=16, null=True)),
                ('product_16_brand', models.CharField(blank=True, max_length=16, null=True)),
                ('product_16_size', models.CharField(blank=True, max_length=16, null=True)),
                ('product_16_color', models.CharField(blank=True, max_length=16, null=True)),
                ('Name_of_product_17', models.CharField(blank=True, max_length=17, null=True)),
                ('product_17_quantity', models.CharField(blank=True, max_length=17, null=True)),
                ('product_17_Price', models.CharField(blank=True, max_length=17, null=True)),
                ('product_17_image_link', models.CharField(blank=True, max_length=17, null=True)),
                ('product_17_brand', models.CharField(blank=True, max_length=17, null=True)),
                ('product_17_size', models.CharField(blank=True, max_length=17, null=True)),
                ('product_17_color', models.CharField(blank=True, max_length=17, null=True)),
                ('Name_of_product_18', models.CharField(blank=True, max_length=18, null=True)),
                ('product_18_quantity', models.CharField(blank=True, max_length=18, null=True)),
                ('product_18_Price', models.CharField(blank=True, max_length=18, null=True)),
                ('product_18_image_link', models.CharField(blank=True, max_length=18, null=True)),
                ('product_18_brand', models.CharField(blank=True, max_length=18, null=True)),
                ('product_18_size', models.CharField(blank=True, max_length=18, null=True)),
                ('product_18_color', models.CharField(blank=True, max_length=18, null=True)),
                ('Name_of_product_19', models.CharField(blank=True, max_length=19, null=True)),
                ('product_19_quantity', models.CharField(blank=True, max_length=19, null=True)),
                ('product_19_Price', models.CharField(blank=True, max_length=19, null=True)),
                ('product_19_image_link', models.CharField(blank=True, max_length=19, null=True)),
                ('product_19_brand', models.CharField(blank=True, max_length=19, null=True)),
                ('product_19_size', models.CharField(blank=True, max_length=19, null=True)),
                ('product_19_color', models.CharField(blank=True, max_length=19, null=True)),
                ('Name_of_product_20', models.CharField(blank=True, max_length=20, null=True)),
                ('product_20_quantity', models.CharField(blank=True, max_length=20, null=True)),
                ('product_20_Price', models.CharField(blank=True, max_length=20, null=True)),
                ('product_20_image_link', models.CharField(blank=True, max_length=20, null=True)),
                ('product_20_brand', models.CharField(blank=True, max_length=20, null=True)),
                ('product_20_size', models.CharField(blank=True, max_length=20, null=True)),
                ('product_20_color', models.CharField(blank=True, max_length=20, null=True)),
                ('Name_of_product_21', models.CharField(blank=True, max_length=21, null=True)),
                ('product_21_quantity', models.CharField(blank=True, max_length=21, null=True)),
                ('product_21_Price', models.CharField(blank=True, max_length=21, null=True)),
                ('product_21_image_link', models.CharField(blank=True, max_length=21, null=True)),
                ('product_21_brand', models.CharField(blank=True, max_length=21, null=True)),
                ('product_21_size', models.CharField(blank=True, max_length=21, null=True)),
                ('product_21_color', models.CharField(blank=True, max_length=21, null=True)),
                ('Name_of_product_22', models.CharField(blank=True, max_length=22, null=True)),
                ('product_22_quantity', models.CharField(blank=True, max_length=22, null=True)),
                ('product_22_Price', models.CharField(blank=True, max_length=22, null=True)),
                ('product_22_image_link', models.CharField(blank=True, max_length=22, null=True)),
                ('product_22_brand', models.CharField(blank=True, max_length=22, null=True)),
                ('product_22_size', models.CharField(blank=True, max_length=22, null=True)),
                ('product_22_color', models.CharField(blank=True, max_length=22, null=True)),
                ('Name_of_product_23', models.CharField(blank=True, max_length=23, null=True)),
                ('product_23_quantity', models.CharField(blank=True, max_length=23, null=True)),
                ('product_23_Price', models.CharField(blank=True, max_length=23, null=True)),
                ('product_23_image_link', models.CharField(blank=True, max_length=23, null=True)),
                ('product_23_brand', models.CharField(blank=True, max_length=23, null=True)),
                ('product_23_size', models.CharField(blank=True, max_length=23, null=True)),
                ('product_23_color', models.CharField(blank=True, max_length=23, null=True)),
                ('Name_of_product_24', models.CharField(blank=True, max_length=24, null=True)),
                ('product_24_quantity', models.CharField(blank=True, max_length=24, null=True)),
                ('product_24_Price', models.CharField(blank=True, max_length=24, null=True)),
                ('product_24_image_link', models.CharField(blank=True, max_length=24, null=True)),
                ('product_24_brand', models.CharField(blank=True, max_length=24, null=True)),
                ('product_24_size', models.CharField(blank=True, max_length=24, null=True)),
                ('product_24_color', models.CharField(blank=True, max_length=24, null=True)),
                ('Name_of_product_25', models.CharField(blank=True, max_length=25, null=True)),
                ('product_25_quantity', models.CharField(blank=True, max_length=25, null=True)),
                ('product_25_Price', models.CharField(blank=True, max_length=25, null=True)),
                ('product_25_image_link', models.CharField(blank=True, max_length=25, null=True)),
                ('product_25_brand', models.CharField(blank=True, max_length=25, null=True)),
                ('product_25_size', models.CharField(blank=True, max_length=25, null=True)),
                ('product_25_color', models.CharField(blank=True, max_length=25, null=True)),
                ('Name_of_product_26', models.CharField(blank=True, max_length=26, null=True)),
                ('product_26_quantity', models.CharField(blank=True, max_length=26, null=True)),
                ('product_26_Price', models.CharField(blank=True, max_length=26, null=True)),
                ('product_26_image_link', models.CharField(blank=True, max_length=26, null=True)),
                ('product_26_brand', models.CharField(blank=True, max_length=26, null=True)),
                ('product_26_size', models.CharField(blank=True, max_length=26, null=True)),
                ('product_26_color', models.CharField(blank=True, max_length=26, null=True)),
                ('Name_of_product_27', models.CharField(blank=True, max_length=27, null=True)),
                ('product_27_quantity', models.CharField(blank=True, max_length=27, null=True)),
                ('product_27_Price', models.CharField(blank=True, max_length=27, null=True)),
                ('product_27_image_link', models.CharField(blank=True, max_length=27, null=True)),
                ('product_27_brand', models.CharField(blank=True, max_length=27, null=True)),
                ('product_27_size', models.CharField(blank=True, max_length=27, null=True)),
                ('product_27_color', models.CharField(blank=True, max_length=27, null=True)),
                ('Name_of_product_28', models.CharField(blank=True, max_length=28, null=True)),
                ('product_28_quantity', models.CharField(blank=True, max_length=28, null=True)),
                ('product_28_Price', models.CharField(blank=True, max_length=28, null=True)),
                ('product_28_image_link', models.CharField(blank=True, max_length=28, null=True)),
                ('product_28_brand', models.CharField(blank=True, max_length=28, null=True)),
                ('product_28_size', models.CharField(blank=True, max_length=28, null=True)),
                ('product_28_color', models.CharField(blank=True, max_length=28, null=True)),
                ('Name_of_product_29', models.CharField(blank=True, max_length=29, null=True)),
                ('product_29_quantity', models.CharField(blank=True, max_length=29, null=True)),
                ('product_29_Price', models.CharField(blank=True, max_length=29, null=True)),
                ('product_29_image_link', models.CharField(blank=True, max_length=29, null=True)),
                ('product_29_brand', models.CharField(blank=True, max_length=29, null=True)),
                ('product_29_size', models.CharField(blank=True, max_length=29, null=True)),
                ('product_29_color', models.CharField(blank=True, max_length=29, null=True)),
                ('Name_of_product_30', models.CharField(blank=True, max_length=30, null=True)),
                ('product_30_quantity', models.CharField(blank=True, max_length=30, null=True)),
                ('product_30_Price', models.CharField(blank=True, max_length=30, null=True)),
                ('product_30_image_link', models.CharField(blank=True, max_length=30, null=True)),
                ('product_30_brand', models.CharField(blank=True, max_length=30, null=True)),
                ('product_30_size', models.CharField(blank=True, max_length=30, null=True)),
                ('product_30_color', models.CharField(blank=True, max_length=30, null=True)),
                ('User_Connect_with_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_one.user_info')),
            ],
            options={
                'verbose_name_plural': 'Order info',
            },
        ),
    ]
