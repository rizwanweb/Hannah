from django.db import models
# Create your models here.
from datetime import datetime
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User



# class User_info(models.Model):
#     class Meta:
#         verbose_name_plural = 'User info'
#
#     User_name = models.CharField(max_length=256, blank=True, null=True)
#     User_mobile = models.CharField(max_length=256, blank=True, null=True)
#     User_pass = models.CharField(max_length=256, blank=True, null=True)
#
#
#     def __str__(self):
#         return self.User_mobile





class Video_Post(models.Model):
    class Meta:
        verbose_name_plural = 'Video Post'

    Video_Title = models.CharField(max_length=256, blank=True, null=True)
    Video_Link = models.TextField( blank=True, null=True)
    Video_content = models.TextField(blank=True, null=True)
    Blog_podt_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return str(self.id)+" "


class Newsletter(models.Model):
    class Meta:
        verbose_name_plural = 'Newsletter'
    Newsletter_name = models.CharField(max_length=256, blank=True, null=True)
    Newsletter_mobile_number = models.TextField( blank=True, null=True)
    Newsletter_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return str(self.id)+" "+ self.Newsletter_mobile_number



class Stay_Updated_subscribtion(models.Model):
    class Meta:
        verbose_name_plural = 'Stay Updated subscribtion'
    Stay_Updated_mobile_number = models.TextField( blank=True, null=True)
    Stay_Updated_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return str(self.id)+" "+ self.Stay_Updated_mobile_number



# class Cosmetics_brand_image(models.Model):
#     class Meta:
#         verbose_name_plural = 'Cosmetics brand image'
#     Cosmetics_brand_image_get = models.ImageField( blank=True, null=True)
#     Cosmetics_brand_image_date = models.DateTimeField(default=datetime.now(), blank=True)
#
#     def __str__(self):
#         return str(self.id)





class Picture_slide(models.Model):
    class Meta:
        verbose_name_plural = 'Banner Picture slide'
    Picture_Title = models.CharField(max_length=256, blank=True, null=True)
    Picture_upload = models.ImageField( blank=True, null=True)
    Picture_content = models.TextField(blank=True, null=True)
    def __str__(self):
        return str(self.id)+" "



class Product_Color(models.Model):
    class Meta:
        verbose_name_plural = 'Product Color'
    Product_Color_name = models.CharField(max_length=256, blank=True, null=True)
    def __str__(self):
        return self.Product_Color_name


class Product_Size(models.Model):
    class Meta:
        verbose_name_plural = 'Product Size'
    Product_Size_name = models.CharField(max_length=256, blank=True, null=True)
    def __str__(self):
        return self.Product_Size_name

class Product_Brand(models.Model):
    class Meta:
        verbose_name_plural = 'Product Brand'
    Product_Brand_name = models.CharField(max_length=256, blank=True, null=True)
    image = models.ImageField(upload_to="banner_image/", default=None, blank=True, null=True)
    def __str__(self):
        return self.Product_Brand_name

#
# class Product_Sub_Caegoty_table(models.Model):
#     class Meta:
#         verbose_name_plural = 'Product Sub Caegoty'
#     Product_Brand_name = models.CharField(max_length=256, blank=True, null=True)
#     def __str__(self):
#         return self.Product_Brand_name
#
#
# class Product_Caegoty_table(models.Model):
#     class Meta:
#         verbose_name_plural = 'Product Caegoty'
#     Product_Brand_name = models.CharField(max_length=256, blank=True, null=True)
#     def __str__(self):
#         return self.Product_Brand_name


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Category'
    Category_Name = models.CharField(max_length=255)
    def __str__(self):
        return self.Category_Name



class Product_details(models.Model):
    class Meta:
        verbose_name_plural = 'Products'

    Product_Title = models.CharField(max_length=256, blank=True, null=True)
    Product_Category = models.ForeignKey(Category, default=None, blank=True, null=True, on_delete=models.CASCADE)
    Product_Picture_upload_1 = models.ImageField( blank=True, null=True, help_text = "Insert 500X500 pixel image")
    Product_Picture_upload_2 = models.ImageField( blank=True, null=True, help_text = "Insert 500X500 pixel image")
    Product_Picture_upload_3 = models.ImageField( blank=True, null=True, help_text = "Insert 500X500 pixel image")
    Product_Picture_upload_4 = models.ImageField( blank=True, null=True, help_text = "Insert 500X500 pixel image")
    Product_Picture_upload_5 = models.ImageField( blank=True, null=True, help_text = "Insert 500X500 pixel image")
    Product_short_details = models.CharField(max_length=256, blank=True, null=True)
    Product_long_details = models.TextField(blank=True, null=True)
    Product_Additional_Information = models.TextField(blank=True, null=True)
    Product_color_Get = models.ManyToManyField(Product_Color, blank=True, null=True)
    # Product_Size_Get = models.ManyToManyField(Product_Size, blank=True, null=True)
    Product_Size_Get = models.CharField(max_length=256, blank=True, null=True)
    Product_Country = models.CharField(max_length=256, blank=True, null=True)
    Product_brand = models.ForeignKey(Product_Brand, on_delete = models.CASCADE, blank=True, null=True)
    Product_Sell_Prize = models.IntegerField(blank=True, null=True)
    Product_Discount_Prize = models.IntegerField(default=0)
    Product_show_type_CHOICES = (
        ('', ''),
        ('You May Also Like', 'You May Also Like'),
        ('Trandy Products', 'Trandy Products'),

    )
    Product_show_type  = models.CharField(max_length=256, choices=Product_show_type_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.Product_Title



class Order_info(models.Model):
    class Meta:
        verbose_name_plural = 'Order info'

    User_Connect_with_order = models.ForeignKey(User, on_delete=models.CASCADE)
    # start from 30000 and add the id after it
    order_No = models.IntegerField(blank=True, null=True)
    perchase_date = models.DateTimeField(default=datetime.now(), blank=True)
    order_User_Name = models.CharField(max_length=256, blank=True, null=True)
    order_User_Mobile = models.CharField(max_length=256, blank=True, null=True)
    order_User_Address = models.CharField(max_length=256, blank=True, null=True)
    order_User_City = models.CharField(max_length=256, blank=True, null=True)
    order_User_ZIP = models.CharField(max_length=256, blank=True, null=True)

    order_User_shipping_charge = models.CharField(max_length=256, blank=True, null=True)
    order_User_Sub_total = models.CharField(max_length=256, blank=True, null=True)
    order_User_total = models.CharField(max_length=256, blank=True, null=True)

    Name_of_product_1 = models.CharField(max_length=256, blank=True, null=True)
    product_1_quantity = models.CharField(max_length=256, blank=True, null=True)
    product_1_Price = models.CharField(max_length=256, blank=True, null=True)
    product_1_image_link = models.CharField(max_length=256, blank=True, null=True)

    product_1_brand = models.CharField(max_length=256, blank=True, null=True)
    product_1_size = models.CharField(max_length=256, blank=True, null=True)
    product_1_color = models.CharField(max_length=256, blank=True, null=True)

    Name_of_product_2 = models.CharField(max_length=256, blank=True, null=True)
    product_2_quantity = models.CharField(max_length=256, blank=True, null=True)
    product_2_Price = models.CharField(max_length=256, blank=True, null=True)
    product_2_image_link = models.CharField(max_length=256, blank=True, null=True)

    product_2_brand = models.CharField(max_length=256, blank=True, null=True)
    product_2_size = models.CharField(max_length=256, blank=True, null=True)
    product_2_color = models.CharField(max_length=256, blank=True, null=True)

    Name_of_product_3 = models.CharField(max_length=356, blank=True, null=True)
    product_3_quantity = models.CharField(max_length=356, blank=True, null=True)
    product_3_Price = models.CharField(max_length=356, blank=True, null=True)
    product_3_image_link = models.CharField(max_length=356, blank=True, null=True)

    product_3_brand = models.CharField(max_length=356, blank=True, null=True)
    product_3_size = models.CharField(max_length=356, blank=True, null=True)
    product_3_color = models.CharField(max_length=356, blank=True, null=True)

    Name_of_product_4 = models.CharField(max_length=456, blank=True, null=True)
    product_4_quantity = models.CharField(max_length=456, blank=True, null=True)
    product_4_Price = models.CharField(max_length=456, blank=True, null=True)
    product_4_image_link = models.CharField(max_length=456, blank=True, null=True)

    product_4_brand = models.CharField(max_length=456, blank=True, null=True)
    product_4_size = models.CharField(max_length=456, blank=True, null=True)
    product_4_color = models.CharField(max_length=456, blank=True, null=True)

    Name_of_product_5 = models.CharField(max_length=556, blank=True, null=True)
    product_5_quantity = models.CharField(max_length=556, blank=True, null=True)
    product_5_Price = models.CharField(max_length=556, blank=True, null=True)
    product_5_image_link = models.CharField(max_length=556, blank=True, null=True)

    product_5_brand = models.CharField(max_length=556, blank=True, null=True)
    product_5_size = models.CharField(max_length=556, blank=True, null=True)
    product_5_color = models.CharField(max_length=556, blank=True, null=True)

    Name_of_product_6 = models.CharField(max_length=66, blank=True, null=True)
    product_6_quantity = models.CharField(max_length=66, blank=True, null=True)
    product_6_Price = models.CharField(max_length=66, blank=True, null=True)
    product_6_image_link = models.CharField(max_length=66, blank=True, null=True)

    product_6_brand = models.CharField(max_length=66, blank=True, null=True)
    product_6_size = models.CharField(max_length=66, blank=True, null=True)
    product_6_color = models.CharField(max_length=66, blank=True, null=True)

    Name_of_product_7 = models.CharField(max_length=7, blank=True, null=True)
    product_7_quantity = models.CharField(max_length=7, blank=True, null=True)
    product_7_Price = models.CharField(max_length=7, blank=True, null=True)
    product_7_image_link = models.CharField(max_length=7, blank=True, null=True)

    product_7_brand = models.CharField(max_length=7, blank=True, null=True)
    product_7_size = models.CharField(max_length=7, blank=True, null=True)
    product_7_color = models.CharField(max_length=7, blank=True, null=True)

    Name_of_product_8 = models.CharField(max_length=8, blank=True, null=True)
    product_8_quantity = models.CharField(max_length=8, blank=True, null=True)
    product_8_Price = models.CharField(max_length=8, blank=True, null=True)
    product_8_image_link = models.CharField(max_length=8, blank=True, null=True)

    product_8_brand = models.CharField(max_length=8, blank=True, null=True)
    product_8_size = models.CharField(max_length=8, blank=True, null=True)
    product_8_color = models.CharField(max_length=8, blank=True, null=True)

    Name_of_product_9 = models.CharField(max_length=9, blank=True, null=True)
    product_9_quantity = models.CharField(max_length=9, blank=True, null=True)
    product_9_Price = models.CharField(max_length=9, blank=True, null=True)
    product_9_image_link = models.CharField(max_length=9, blank=True, null=True)

    product_9_brand = models.CharField(max_length=9, blank=True, null=True)
    product_9_size = models.CharField(max_length=9, blank=True, null=True)
    product_9_color = models.CharField(max_length=9, blank=True, null=True)

    Name_of_product_10 = models.CharField(max_length=10, blank=True, null=True)
    product_10_quantity = models.CharField(max_length=10, blank=True, null=True)
    product_10_Price = models.CharField(max_length=10, blank=True, null=True)
    product_10_image_link = models.CharField(max_length=10, blank=True, null=True)

    product_10_brand = models.CharField(max_length=10, blank=True, null=True)
    product_10_size = models.CharField(max_length=10, blank=True, null=True)
    product_10_color = models.CharField(max_length=10, blank=True, null=True)

    Name_of_product_11 = models.CharField(max_length=11, blank=True, null=True)
    product_11_quantity = models.CharField(max_length=11, blank=True, null=True)
    product_11_Price = models.CharField(max_length=11, blank=True, null=True)
    product_11_image_link = models.CharField(max_length=11, blank=True, null=True)

    product_11_brand = models.CharField(max_length=11, blank=True, null=True)
    product_11_size = models.CharField(max_length=11, blank=True, null=True)
    product_11_color = models.CharField(max_length=11, blank=True, null=True)

    Name_of_product_12 = models.CharField(max_length=12, blank=True, null=True)
    product_12_quantity = models.CharField(max_length=12, blank=True, null=True)
    product_12_Price = models.CharField(max_length=12, blank=True, null=True)
    product_12_image_link = models.CharField(max_length=12, blank=True, null=True)

    product_12_brand = models.CharField(max_length=12, blank=True, null=True)
    product_12_size = models.CharField(max_length=12, blank=True, null=True)
    product_12_color = models.CharField(max_length=12, blank=True, null=True)

    Name_of_product_13 = models.CharField(max_length=13, blank=True, null=True)
    product_13_quantity = models.CharField(max_length=13, blank=True, null=True)
    product_13_Price = models.CharField(max_length=13, blank=True, null=True)
    product_13_image_link = models.CharField(max_length=13, blank=True, null=True)

    product_13_brand = models.CharField(max_length=13, blank=True, null=True)
    product_13_size = models.CharField(max_length=13, blank=True, null=True)
    product_13_color = models.CharField(max_length=13, blank=True, null=True)

    Name_of_product_14 = models.CharField(max_length=14, blank=True, null=True)
    product_14_quantity = models.CharField(max_length=14, blank=True, null=True)
    product_14_Price = models.CharField(max_length=14, blank=True, null=True)
    product_14_image_link = models.CharField(max_length=14, blank=True, null=True)

    product_14_brand = models.CharField(max_length=14, blank=True, null=True)
    product_14_size = models.CharField(max_length=14, blank=True, null=True)
    product_14_color = models.CharField(max_length=14, blank=True, null=True)

    Name_of_product_15 = models.CharField(max_length=15, blank=True, null=True)
    product_15_quantity = models.CharField(max_length=15, blank=True, null=True)
    product_15_Price = models.CharField(max_length=15, blank=True, null=True)
    product_15_image_link = models.CharField(max_length=15, blank=True, null=True)

    product_15_brand = models.CharField(max_length=15, blank=True, null=True)
    product_15_size = models.CharField(max_length=15, blank=True, null=True)
    product_15_color = models.CharField(max_length=15, blank=True, null=True)

    Name_of_product_16 = models.CharField(max_length=16, blank=True, null=True)
    product_16_quantity = models.CharField(max_length=16, blank=True, null=True)
    product_16_Price = models.CharField(max_length=16, blank=True, null=True)
    product_16_image_link = models.CharField(max_length=16, blank=True, null=True)

    product_16_brand = models.CharField(max_length=16, blank=True, null=True)
    product_16_size = models.CharField(max_length=16, blank=True, null=True)
    product_16_color = models.CharField(max_length=16, blank=True, null=True)

    Name_of_product_17 = models.CharField(max_length=17, blank=True, null=True)
    product_17_quantity = models.CharField(max_length=17, blank=True, null=True)
    product_17_Price = models.CharField(max_length=17, blank=True, null=True)
    product_17_image_link = models.CharField(max_length=17, blank=True, null=True)

    product_17_brand = models.CharField(max_length=17, blank=True, null=True)
    product_17_size = models.CharField(max_length=17, blank=True, null=True)
    product_17_color = models.CharField(max_length=17, blank=True, null=True)

    Name_of_product_18 = models.CharField(max_length=18, blank=True, null=True)
    product_18_quantity = models.CharField(max_length=18, blank=True, null=True)
    product_18_Price = models.CharField(max_length=18, blank=True, null=True)
    product_18_image_link = models.CharField(max_length=18, blank=True, null=True)

    product_18_brand = models.CharField(max_length=18, blank=True, null=True)
    product_18_size = models.CharField(max_length=18, blank=True, null=True)
    product_18_color = models.CharField(max_length=18, blank=True, null=True)

    Name_of_product_19 = models.CharField(max_length=19, blank=True, null=True)
    product_19_quantity = models.CharField(max_length=19, blank=True, null=True)
    product_19_Price = models.CharField(max_length=19, blank=True, null=True)
    product_19_image_link = models.CharField(max_length=19, blank=True, null=True)

    product_19_brand = models.CharField(max_length=19, blank=True, null=True)
    product_19_size = models.CharField(max_length=19, blank=True, null=True)
    product_19_color = models.CharField(max_length=19, blank=True, null=True)

    Name_of_product_20 = models.CharField(max_length=20, blank=True, null=True)
    product_20_quantity = models.CharField(max_length=20, blank=True, null=True)
    product_20_Price = models.CharField(max_length=20, blank=True, null=True)
    product_20_image_link = models.CharField(max_length=20, blank=True, null=True)

    product_20_brand = models.CharField(max_length=20, blank=True, null=True)
    product_20_size = models.CharField(max_length=20, blank=True, null=True)
    product_20_color = models.CharField(max_length=20, blank=True, null=True)

    Name_of_product_21 = models.CharField(max_length=21, blank=True, null=True)
    product_21_quantity = models.CharField(max_length=21, blank=True, null=True)
    product_21_Price = models.CharField(max_length=21, blank=True, null=True)
    product_21_image_link = models.CharField(max_length=21, blank=True, null=True)

    product_21_brand = models.CharField(max_length=21, blank=True, null=True)
    product_21_size = models.CharField(max_length=21, blank=True, null=True)
    product_21_color = models.CharField(max_length=21, blank=True, null=True)

    Name_of_product_22 = models.CharField(max_length=22, blank=True, null=True)
    product_22_quantity = models.CharField(max_length=22, blank=True, null=True)
    product_22_Price = models.CharField(max_length=22, blank=True, null=True)
    product_22_image_link = models.CharField(max_length=22, blank=True, null=True)

    product_22_brand = models.CharField(max_length=22, blank=True, null=True)
    product_22_size = models.CharField(max_length=22, blank=True, null=True)
    product_22_color = models.CharField(max_length=22, blank=True, null=True)

    Name_of_product_23 = models.CharField(max_length=23, blank=True, null=True)
    product_23_quantity = models.CharField(max_length=23, blank=True, null=True)
    product_23_Price = models.CharField(max_length=23, blank=True, null=True)
    product_23_image_link = models.CharField(max_length=23, blank=True, null=True)

    product_23_brand = models.CharField(max_length=23, blank=True, null=True)
    product_23_size = models.CharField(max_length=23, blank=True, null=True)
    product_23_color = models.CharField(max_length=23, blank=True, null=True)

    Name_of_product_24 = models.CharField(max_length=24, blank=True, null=True)
    product_24_quantity = models.CharField(max_length=24, blank=True, null=True)
    product_24_Price = models.CharField(max_length=24, blank=True, null=True)
    product_24_image_link = models.CharField(max_length=24, blank=True, null=True)

    product_24_brand = models.CharField(max_length=24, blank=True, null=True)
    product_24_size = models.CharField(max_length=24, blank=True, null=True)
    product_24_color = models.CharField(max_length=24, blank=True, null=True)

    Name_of_product_25 = models.CharField(max_length=25, blank=True, null=True)
    product_25_quantity = models.CharField(max_length=25, blank=True, null=True)
    product_25_Price = models.CharField(max_length=25, blank=True, null=True)
    product_25_image_link = models.CharField(max_length=25, blank=True, null=True)

    product_25_brand = models.CharField(max_length=25, blank=True, null=True)
    product_25_size = models.CharField(max_length=25, blank=True, null=True)
    product_25_color = models.CharField(max_length=25, blank=True, null=True)

    Name_of_product_26 = models.CharField(max_length=26, blank=True, null=True)
    product_26_quantity = models.CharField(max_length=26, blank=True, null=True)
    product_26_Price = models.CharField(max_length=26, blank=True, null=True)
    product_26_image_link = models.CharField(max_length=26, blank=True, null=True)

    product_26_brand = models.CharField(max_length=26, blank=True, null=True)
    product_26_size = models.CharField(max_length=26, blank=True, null=True)
    product_26_color = models.CharField(max_length=26, blank=True, null=True)

    Name_of_product_27 = models.CharField(max_length=27, blank=True, null=True)
    product_27_quantity = models.CharField(max_length=27, blank=True, null=True)
    product_27_Price = models.CharField(max_length=27, blank=True, null=True)
    product_27_image_link = models.CharField(max_length=27, blank=True, null=True)

    product_27_brand = models.CharField(max_length=27, blank=True, null=True)
    product_27_size = models.CharField(max_length=27, blank=True, null=True)
    product_27_color = models.CharField(max_length=27, blank=True, null=True)

    Name_of_product_28 = models.CharField(max_length=28, blank=True, null=True)
    product_28_quantity = models.CharField(max_length=28, blank=True, null=True)
    product_28_Price = models.CharField(max_length=28, blank=True, null=True)
    product_28_image_link = models.CharField(max_length=28, blank=True, null=True)

    product_28_brand = models.CharField(max_length=28, blank=True, null=True)
    product_28_size = models.CharField(max_length=28, blank=True, null=True)
    product_28_color = models.CharField(max_length=28, blank=True, null=True)

    Name_of_product_29 = models.CharField(max_length=29, blank=True, null=True)
    product_29_quantity = models.CharField(max_length=29, blank=True, null=True)
    product_29_Price = models.CharField(max_length=29, blank=True, null=True)
    product_29_image_link = models.CharField(max_length=29, blank=True, null=True)

    product_29_brand = models.CharField(max_length=29, blank=True, null=True)
    product_29_size = models.CharField(max_length=29, blank=True, null=True)
    product_29_color = models.CharField(max_length=29, blank=True, null=True)

    Name_of_product_30 = models.CharField(max_length=30, blank=True, null=True)
    product_30_quantity = models.CharField(max_length=30, blank=True, null=True)
    product_30_Price = models.CharField(max_length=30, blank=True, null=True)
    product_30_image_link = models.CharField(max_length=30, blank=True, null=True)

    product_30_brand = models.CharField(max_length=30, blank=True, null=True)
    product_30_size = models.CharField(max_length=30, blank=True, null=True)
    product_30_color = models.CharField(max_length=30, blank=True, null=True)



    # def save(self):
    #     self.Order_info = self.Coin + self.Coin_deposit - self.Coin_escrow - self.Withdraw_escrow + self.earn_from_escrow + self.earn_from_micro_job - self.use_in_micro_job
    #     return super(Order_info, self).save()



    def __str__(self):
        return self.order_User_Mobile


class contact_table(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Table'
    Email = models.CharField(max_length=255)
    Subject = models.CharField(max_length=255)
    Message = models.TextField()
    def __str__(self):
        return self.Email



