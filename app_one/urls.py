from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('Live_Video/', views.Live_Video, name='Live_Video'),
    path('checkout/', views.checkout, name='checkout'),
    path('details/<int:pk>', views.details, name='details'),
    path('save_order/', views.save_order, name='save_order'),
    path('login_func/', views.login_func, name='login_func'),
    path('reg/', views.reg, name='reg'),

    path('cheak_email_from_def/', views.cheak_email_from_def, name='cheak_email_from_def'),
    path('regis/', views.regis, name='regis'),
    path('Log_in/', views.Log_in, name='Log_in'),
    path('Log_out/', views.Log_out, name='Log_out'),

    path('Previous_order/', views.Previous_order, name='Previous_order'),
    path('Change_Password/', views.Change_Password, name='Change_Password'),
    path('save_change_pass/', views.save_change_pass, name='save_change_pass'),
    path('order_No_show/<int:pk>', views.order_No_show, name='order_No_show'),


    path('Newsletter_get/', views.Newsletter_get, name='Newsletter_get'),
    path('Stay_Updated_get/', views.Stay_Updated_get, name='Stay_Updated_get'),
    path('Shop_Now/', views.Shop_Now, name='Shop_Now'),

    path('search_button_def/', views.search_button_def, name='search_button_def'),
    path('Trandy_Products_See_More/', views.Trandy_Products_See_More, name='Trandy_Products_See_More'),
    path('You_May_Also_Like/', views.You_May_Also_Like, name='You_May_Also_Like'),


    path('Face_Care/', views.Face_Care, name='Face_Care'),
    path('Body_Care/', views.Body_Care, name='Body_Care'),
    path('Soothing_Gel/', views.Soothing_Gel, name='Soothing_Gel'),
    path('Serum/', views.Serum, name='Serum'),
    path('Night_Cream_And_Day_Cream/', views.Night_Cream_And_Day_Cream, name='Night_Cream_And_Day_Cream'),
    path('Sunscreen/', views.Sunscreen, name='Sunscreen'),
    path('Face_Pack/', views.Face_Pack, name='Face_Pack'),
    path('Massage_Cream/', views.Massage_Cream, name='Massage_Cream'),
    path('Scrub/', views.Scrub, name='Scrub'),
    path('Face_Wsah/', views.Face_Wsah, name='Face_Wsah'),
    path('Bath_Salt/', views.Bath_Salt, name='Bath_Salt'),
    path('Hear_Remover/', views.Hear_Remover, name='Hear_Remover'),
    path('Foot_Cream/', views.Foot_Cream, name='Foot_Cream'),
    path('Moisturizing_Cream/', views.Moisturizing_Cream, name='Moisturizing_Cream'),
    path('Toner/', views.Toner, name='Toner'),
    path('Lip_Care/', views.Lip_Care, name='Lip_Care'),
    path('Eye_Care/', views.Eye_Care, name='Eye_Care'),
    path('Skin_Concern/', views.Skin_Concern, name='Skin_Concern'),
    path('Shampoo/', views.Shampoo, name='Shampoo'),
    path('Hear_Oil/', views.Hear_Oil, name='Hear_Oil'),
    path('Hear_Tonic/', views.Hear_Tonic, name='Hear_Tonic'),
    path('Hear_Mask/', views.Hear_Mask, name='Hear_Mask'),
    path('Hear_Treatment/', views.Hear_Treatment, name='Hear_Treatment'),
    path('Hear_Serum/', views.Hear_Serum, name='Hear_Serum'),
    path('Conditioner/', views.Conditioner, name='Conditioner'),
    path('Face/', views.Face, name='Face'),
    path('Eyes/', views.Eyes, name='Eyes'),
    path('Lips/', views.Lips, name='Lips'),
    path('Nails/', views.Nails, name='Nails'),
    path('Brushes_and_Accessories/', views.Brushes_and_Accessories, name='Brushes_and_Accessories'),

    path('Health_care/', views.Health_care, name='Health_care'),
    path('Category_product/<int:pk>', views.Category_product, name='Category_product'),
    path('Contact/', views.Contact, name='Contact'),
    path('searchbar', views.searchbar, name='searchbar'),
    path('brand_product', views.brand_product, name='brand_product'),



]
