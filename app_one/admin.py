from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin


class Bran(ImportExportModelAdmin):
    pass


# Register your models here.
admin.site.register(Category),
admin.site.register(contact_table),
# admin.site.register(Video_Post),
admin.site.register(Picture_slide),
admin.site.register(Product_details, Bran),
admin.site.register(Product_Color),
admin.site.register(Product_Size),
admin.site.register(Product_Brand),
# admin.site.register(User_info, Bran),
admin.site.register(Order_info, Bran),
admin.site.register(Newsletter, Bran),
admin.site.register(Stay_Updated_subscribtion, Bran),
# admin.site.register(Cosmetics_brand_image),
